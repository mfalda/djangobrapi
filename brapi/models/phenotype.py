from django.db import models
from rest_framework import serializers

from brapi.models.observation import Observation


class Phenotype(models.Model):

    observationUnitDbId = models.CharField(max_length=100, blank=True, default='')
    observationLevel = models.CharField(max_length=100, blank=True, default='')
    observationLevels = models.CharField(max_length=100, null=True, default='')
    plotNumber = models.CharField(max_length=100, null=True, default='')
    plantNumber = models.IntegerField(null=True)
    blockNumber = models.IntegerField(null=True)
    replicate = models.IntegerField(null=True)
    observationUnitName = models.CharField(max_length=100, blank=True, default='')
    germplasmDbId = models.CharField(max_length=100, blank=True, default='')
    germplasmName = models.CharField(max_length=100, blank=True, default='')
    studyDbId = models.CharField(max_length=100, blank=True, default='')
    studyName = models.CharField(max_length=100, blank=True, default='')
    studyLocationDbId = models.CharField(max_length=100, blank=True, default='')
    studyLocation = models.CharField(max_length=100, blank=True, default='')
    programName = models.CharField(max_length=100, blank=True, default='')
    X = models.IntegerField(null=True)
    Y = models.IntegerField(null=True)
    entryType = models.CharField(max_length=100, null=True, default='')
    entryNumber = models.IntegerField(null=True)
    treatments = models.IntegerField(null=True)
    observationUnitXref = models.IntegerField(null=True)
    observations = models.ForeignKey(Observation, db_column='observations', related_name='observations', on_delete=models.CASCADE, default='', to_field='observationDbId')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Phenotype
    
    
class PhenotypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Phenotype
        exclude = ['id']

    # end class Meta

# end class PhenotypeSerializer

