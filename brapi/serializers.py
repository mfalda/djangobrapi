from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from brapi.models import Call, Location, Crop
from brapi.apps import BrAPIListPagination


class StringListField(serializers.ListField):
    
    child = serializers.CharField(max_length=10, default='GET')

 # end class StringListField


 # using hyperlinks and URLs instead of RDBMs IDs and foreign keys
class CallsSerializer(serializers.HyperlinkedModelSerializer):

    datatypes = StringListField()
    methods = StringListField()


    class Meta:

        model = Call
        fields = ('call', 'datatypes', 'methods')

    # end class Meta


    def to_representation(self, instance: Call):
        
        instance.datatypes = [str(s) for s in instance.datatypes.split('; ')]
        instance.methods = [str(s) for s in instance.methods.split('; ')]

        return super(CallsSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(CallsSerializer, self).to_internal_value(data)

        if ret['datatypes']:
            ret['datatypes'] = '; '.join(str(s) for s in ret['datatypes'])
        # end if

        if ret['methods']:
            ret['methods'] = '; '.join(str(s) for s in ret['methods'])
        # end if

        return ret

    # end def to_internal_value


# end class CallsSerializer


class CropSerializer(serializers.HyperlinkedModelSerializer):
    
    # when the URL name is different from the model name
    #url = serializers.HyperlinkedIdentityField(view_name="crops-detail")
    pagination_class = BrAPIListPagination

    class Meta:

        model = Crop
        fields = ['data']

    # end class Meta

# end class CropSerializer


class LocationSerializer(serializers.HyperlinkedModelSerializer):

    # when the URL name is different from the model name
    url = serializers.HyperlinkedIdentityField(view_name="locations-detail")
    
    class Meta:

        model = Location
        fields = '__all__'

    # end class Meta

# end class LocationSerializer