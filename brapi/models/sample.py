from django.db import models
from rest_framework import serializers

from brapi.aux_types import SeasonType


class Sample(models.Model):

    studyDbId = models.CharField(max_length=100, blank=True, default='')
    locationDbId = models.CharField(max_length=100, blank=True, default='')
    plotId = models.CharField(max_length=100, blank=True, default='')
    plantId = models.CharField(max_length=100, blank=True, default='')
    sampleId = models.CharField(max_length=100, blank=True, default='')
    takenBy = models.CharField(max_length=100, blank=True, default='')
    sampleTimestamp = models.DateTimeField(max_length=100, blank=True, default='')
    sampleType = models.CharField(max_length=100, blank=True, default='')
    tissueType = models.CharField(max_length=100, blank=True, default='')
    notes = models.CharField(max_length=100, blank=True, default='')
    studyName = models.CharField(max_length=100, blank=True, default='')
    season = models.CharField(max_length=100, blank=True, choices=SeasonType.choices())
    locationName = models.CharField(max_length=100, blank=True, default='')
    entryNumber = models.IntegerField()
    plotNumber = models.IntegerField()
    germplasmDbId = models.IntegerField()
    plantingTimestamp = models.DateTimeField()
    harvestTimestamp = models.DateTimeField()


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Sample


class SampleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sample
        exclude = ['id']

    # end class Meta

# end class SampleSerializer
