from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from brapi.models import Call


class StringListField(serializers.ListField):
    
    child = serializers.CharField(max_length=10, default='GET')

 # end class StringListField


 # using hyperlinks and URLs instead of RDBMs IDs and foreign keys
class CallsSerializer(serializers.HyperlinkedModelSerializer):

    email = models.CharField(max_length=100, blank=True, default='')
    datatypes_list = StringListField()
    methods_list = StringListField()


    class Meta:
        model = Call
        fields = ('call', 'datatypes_list', 'methods_list')

    # end class Meta


    def to_representation(self, instance: Call):
        
        instance.datatypes_list = [str(s) for s in instance.datatypes.split('; ')]
        instance.methods_list = [str(s) for s in instance.methods.split('; ')]

        return super(CallsSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(CallsSerializer, self).to_internal_value(data)

        if ret['datatypes_list']:
            ret['datatypes'] = '; '.join(str(s) for s in ret['datatypes_list'])
        # end if

        if ret['methods_list']:
            ret['methods'] = '; '.join(str(s) for s in ret['methods_list'])
        # end if

        return ret

    # end def to_internal_value


# end class CallsSerializer

