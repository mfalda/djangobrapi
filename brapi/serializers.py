from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User

from brapi.models import Call, Location, Crop, Program, Map, MapLinkage, Marker, Trait


class StringListField(serializers.ListField):
    
    child = serializers.CharField(max_length=10, default='GET')

 # end class StringListField


 # using hyperlinks and URLs instead of RDBMs IDs and foreign keys
class CallsSerializer(serializers.ModelSerializer):

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


class ProgramSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Program
        fields = '__all__'

    # end class Meta

# end class ProgramSerializer


class CropSerializer(serializers.ModelSerializer):
    
    # when the URL name is different from the model name
    #url = serializers.HyperlinkedIdentityField(view_name="crops-detail")

    class Meta:

        model = Crop
        fields = ['data']

    # end class Meta

# end class CropSerializer


class MapLinkageSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = MapLinkage
        fields = ['mapDbId', 'markerDbId', 'markerName', 'location', 'linkageGroupId']

    # end class Meta

# end class MapLinkageSerializer


class MapSerializer(serializers.ModelSerializer):
    
    linkageGroups = MapLinkageSerializer(many=True, read_only=True)

    class Meta:

        model = Map
        fields = ['mapDbId', 'name', 'species', 'type', 'unit', 'publishedDate', 
                    'markerCount', 'comments', 'linkageGroups']

    # end class Meta

# end class MapSerializer

 
class MapLinkageSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = MapLinkage
        fields = '__all__'

    # end class Meta

# end class MapLinkageSerializer


class LocationSerializer(serializers.ModelSerializer):
  
    class Meta:

        model = Location
        fields = '__all__'

    # end class Meta

# end class LocationSerializer


class MarkerSerializer(serializers.ModelSerializer):

    synonyms = StringListField()   
    refAlt = StringListField()   
    analysisMethods = StringListField()   

    class Meta:

        model = Marker
        fields = ('markerDbId', 'defaultDisplayName', 'type', 'synonyms', 'refAlt', 'analysisMethods')

    # end class Meta

        
    def to_representation(self, instance: Call):
        
        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]
        instance.refAlt = [str(s) for s in instance.refAlt.split('; ')]
        instance.analysisMethods = [str(s) for s in instance.analysisMethods.split('; ')]

        return super(MarkerSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(CallsSerializer, self).to_internal_value(data)

        if ret['synonyms']:
            ret['synonyms'] = '; '.join(str(s) for s in ret['synonyms'])
        # end if

        if ret['refAlt']:
            ret['refAlt'] = '; '.join(str(s) for s in ret['refAlt'])
        # end if

        if ret['analysisMethods']:
            ret['analysisMethods'] = '; '.join(str(s) for s in ret['analysisMethods'])
        # end if

        return ret

    # end def to_internal_value

# end class MarkerSerializer


class TraitSerializer(serializers.ModelSerializer):

    observationVariables = StringListField()

    class Meta:

        model = Trait
        fields = ['traitDbId', 'traitId', 'name', 'description', 'observationVariables', 'defaultValue']

    # end class Meta


    def to_representation(self, instance: Call):
        
        instance.observationVariables = [str(s) for s in instance.observationVariables.split('; ')]

        return super(TraitSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(TraitSerializer, self).to_internal_value(data)

        if ret['observationVariables']:
            ret['observationVariables'] = '; '.join(str(s) for s in ret['observationVariables'])
        # end if

        return ret

    # end def to_internal_value
    
# end class TraitSerializer