from django.db import models
from rest_framework import serializers

from brapi.aux_types import StringListField


class Datatype(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Datatype


class Ontology(models.Model):
    
    ontologyDbId = models.CharField(max_length=100, blank=True, default='')
    ontologyName = models.CharField(max_length=100, blank=True, default='')
    authors = models.CharField(max_length=100, blank=True, default='')
    version = models.CharField(max_length=100, blank=True, default='')
    copyright = models.CharField(max_length=100, null=True, default='')
    licence = models.CharField(max_length=100, null=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Ontology


class ObsVValue(models.Model):
    
    min = models.IntegerField()
    max = models.IntegerField()
    categories = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.categories = '; '.join(self.categories)

    # end def save


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class ObsVValue


class ObsMethod(models.Model):
    
    methodDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    classe = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    formula = models.CharField(max_length=100, blank=True, default='')
    reference = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class ObsMethod


class ObsScale(models.Model):
    
    scaleDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    datatype = models.CharField(max_length=100, blank=True, default='')
    decimalPlaces = models.CharField(max_length=100, blank=True, default='')
    xref = models.CharField(max_length=100, null=True, default='')
    validValues = models.ForeignKey(ObsVValue, db_column='validValues', related_name='validValues', on_delete=models.CASCADE, default='', to_field='id')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class ObsScale


class ObsTrait(models.Model):

    traitDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    classe = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    synonyms = models.CharField(max_length=100, blank=True, default='')
    mainAbbreviation = models.CharField(max_length=100, blank=True, default='')
    alternativeAbbreviations = models.CharField(max_length=100, blank=True, default='')
    entity = models.CharField(max_length=100, blank=True, default='')
    attribute = models.CharField(max_length=100, null=True, default='')
    status = models.CharField(max_length=100, blank=True, default='')
    xref = models.CharField(max_length=100, blank=True, default='')
    uniqueDisplayName = models.CharField(max_length=100, blank=True, default='')
    extractDbId = models.IntegerField(null=True)
    markerprofileDbId = models.IntegerField(null=True)
    analysisMethod = models.CharField(max_length=100, blank=True, default='')
    data = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class ObsTrait


class ObsVariable(models.Model):
    
    observationVariableDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    ontologyDbId = models.CharField(max_length=100, blank=True, default='')
    ontologyName = models.CharField(max_length=100, blank=True, default='')
    synonyms = models.CharField(max_length=100, null=True, default='')
    contextOfUse = models.CharField(max_length=100, null=True, default='')
    growthStage = models.CharField(max_length=100, null=True, default='')
    status = models.CharField(max_length=100, null=True, default='')
    xref = models.CharField(max_length=100, null=True, default='')
    institution = models.CharField(max_length=100, null=True, default='')
    scientist = models.CharField(max_length=100, null=True, default='')
    date = models.DateField()
    language = models.CharField(max_length=100, null=True, default='')
    crop = models.CharField(max_length=100, null=True, default='')
    defaultValue = models.CharField(max_length=100, null=True, default='')
    trait = models.ForeignKey(ObsTrait, db_column='trait', related_name='trait', on_delete=models.CASCADE, default='', to_field='traitDbId')
    method = models.ForeignKey(ObsMethod, db_column='method', related_name='method', on_delete=models.CASCADE, default='', to_field='methodDbId')
    scale = models.ForeignKey(ObsScale, db_column='scale', related_name='scale', on_delete=models.CASCADE, default='', to_field='scaleDbId')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class ObsVariable


class Observation(models.Model):

    observationDbId = models.IntegerField(unique=True)
    observationVariableDbId = models.ForeignKey(ObsVariable, db_column='observations', related_name='observation_variables', on_delete=models.CASCADE, default='', to_field='observationVariableDbId')
    observationVariableName = models.CharField(max_length=100, blank=True, default='')
    observationTimeStamp = models.DateTimeField()
    season = models.CharField(max_length=100, blank=True, default='')
    collector = models.CharField(max_length=100, blank=True, default='')
    value = models.IntegerField()


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Observation
    
    
class DatatypeSerializer(serializers.ModelSerializer):
    
     class Meta:

        model = Datatype
        fields = ['data']

    # end class Meta

# end class DatatypeSerializer


class OntologySerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Ontology
        exclude = ['id']

    # end class Meta

# end class OntologySerializer
    
    
class ObsVValueSerializer(serializers.ModelSerializer):
        
    categories = StringListField()


    class Meta:

        model = ObsVValue
        exclude = ['id']

    # end class Meta


    def to_representation(self, instance: ObsVValue):
    
        instance.categories = [str(s) for s in instance.categories.split('; ')]

        return super(ObsVValueSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(ObsVValueSerializer, self).to_internal_value(self.categories)

        if ret['categories']:
            ret['categories'] = '; '.join(str(s) for s in ret['categories'])
        # end if

        return ret

    # end def to_internal_value
    
# end class ObsVValueSerializer


class ObsMethodSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = ObsMethod
        exclude = ['id']

    # end class Meta

# end class ObsMethodSerializer


class ObsScaleSerializer(serializers.ModelSerializer):
    
    validValues = ObsVValueSerializer(read_only=True)

    class Meta:

        model = ObsScale
        exclude = ['id']

    # end class Meta

# end class ObsScaleSerializer


class ObsTraitSerializer(serializers.ModelSerializer):

    class Meta:

        model = ObsTrait
        exclude = ['id']

    # end class Meta

 # end class ObsTraitSerializer


class ObsVariableSerializer(serializers.ModelSerializer):
    
    method = ObsMethodSerializer(read_only=True)
    trait = ObsTraitSerializer(read_only=True)
    scale = ObsScaleSerializer(read_only=True)

    class Meta:

        model = ObsVariable
        exclude = ['id']

    # end class Meta
 
# end class ObsVariableSerializer


class ObservationUnitXref(models.Model):

    ouXrefId = models.IntegerField()
    source = models.CharField(max_length=100, blank=True, default='')
    id = models.CharField(db_column='id_field', primary_key=True, max_length=100, default='')

# end class ObservationUnitXref
