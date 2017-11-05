from django.db import models
from rest_framework import serializers

from brapi.models.observation import (ObsMethodSerializer, ObsTraitSerializer,
                                      ObsScaleSerializer)

from brapi.aux_types import StringListField


class Trial(models.Model):

    trialDbId = models.IntegerField(unique=True)
    trialName = models.CharField(max_length=100, blank=True, default='')
    programDbId = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default='')
    startDate = models.DateField()
    endDate = models.DateField()
    active = models.BooleanField()

# end class Trial
    
    
class Treatment(models.Model):

    treatmentId = models.IntegerField()
    factor = models.CharField(max_length=100, blank=True, default='')
    modality = models.CharField(max_length=100, blank=True, default='')

# end class Treatment


class DataLink(models.Model):

    type = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    url = models.CharField(max_length=100, blank=True, default='')

# end class DataLink
    
    
class StudySeason(models.Model):
    
    seasonDbId = models.IntegerField(primary_key=True, db_column='id')
    season = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField()

# end class StudySeason


class StudyType(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')

# end class StudyType


class StudyObsLevel(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')

# end class StudyObsLevel


class StudyPlot(models.Model):
    
    studyDbId = models.IntegerField()
    observationUnitDbId = models.IntegerField()
    observationUnitName = models.CharField(max_length=100, blank=True, default='')
    observationLevel = models.CharField(max_length=100, blank=True, default='')
    replicate = models.IntegerField()
    germplasmDbId = models.IntegerField()
    germplasmName = models.CharField(max_length=100, blank=True, default='')
    blockNumber = models.IntegerField()
    X = models.IntegerField()
    Y = models.IntegerField()
    entryType = models.CharField(max_length=100, blank=True, default='')

# end class StudyPlot

    
class Study(models.Model):
    
    studyDbId = models.IntegerField()
    studyName = models.CharField(max_length=100, blank=True, default='')
    trialDbId = models.ForeignKey(Trial, db_column='trialDbId', related_name='studies', on_delete=models.CASCADE, default='', to_field='trialDbId')
    locationName = models.CharField(max_length=100, blank=True, default='')
    trialName = models.CharField(max_length=100, blank=True, default='')
    studyType = models.CharField(max_length=100, blank=True, default='')
    seasons = models.CharField(max_length=100, blank=True, default='')
    locationDbId = models.IntegerField()
    locationName = models.CharField(max_length=100, blank=True, default='')
    programDbId = models.IntegerField()
    programName = models.CharField(max_length=100, blank=True, default='')
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    active = models.BooleanField()
    contactDbId = models.CharField(max_length=100, blank=True, default='')
    dataLinks = models.ForeignKey(DataLink, db_column='dataLinks', related_name='dataLinks', on_delete=models.CASCADE, default='', to_field='id')
    lastUpdate = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.contactDbId = '; '.join(self.contactDbId)

    # end def save
    
# end class Study


class StudyObsUnit(models.Model):
    
    studyDbId = models.IntegerField()
    observationDbId = models.IntegerField(null=True)
    observationUnitDbId = models.IntegerField(null=True)
    observationUnitName = models.CharField(max_length=100, blank=True, default='')
    observationLevel = models.CharField(max_length=100, blank=True, default='')
    observationVariableDbId = models.IntegerField(null=True)
    observationVariableName = models.CharField(max_length=100, blank=True, default='')
    observationTimestamp = models.DateTimeField()
    uploadedBy = models.CharField(max_length=100, blank=True, default='')
    operator = models.CharField(max_length=100, blank=True, default='')
    germplasmDbId = models.IntegerField(null=True)
    germplasmName = models.IntegerField(null=True)
    value = models.IntegerField(null=True)
    
# end class StudyObsUnit
    
    
class StudySeasonSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = StudySeason
        fields = '__all__'

    # end class Meta

# end class StudySeasonSerializer


class StudyTypeSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = StudyType
        exclude = ['id']

    # end class Meta

# end class StudyTypeSerializer


class StudyObsLevelSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = StudyObsLevel
        exclude = ['id']

    # end class Meta

# end class StudyObsLevelSerializer


class StudyPlotSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = StudyPlot
        exclude = ['id']

    # end class Meta

# end class StudyPlotSerializer


class StudyObsUnitSerializer(serializers.ModelSerializer):
    
    method = ObsMethodSerializer(read_only=True)
    trait = ObsTraitSerializer(read_only=True)
    scale = ObsScaleSerializer(read_only=True)

    class Meta:

        model = StudyObsUnit
        exclude = ['id']

    # end class Meta
 
# end class StudyObsUnitSerializer


class StudySerializer(serializers.ModelSerializer):

    studies = StringListField()
    
    
    class Meta:

        model = Study
        fields = ['studyDbId', 'studyName', 'locationName']

    # end class Meta


    def to_representation(self, instance: Study):
    
        instance.contactDbId = [str(s) for s in instance.contactDbId.split('; ')]

        return super(StudySerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(StudySerializer, self).to_internal_value(data)

        if ret['contactDbId']:
            ret['contactDbId'] = '; '.join(str(s) for s in ret['contactDbId'])
        # end if

        return ret

    # end def to_internal_value
    
# end class StudySerializer


class TrialSerializer(serializers.ModelSerializer):

    studies = StudySerializer(many=True, read_only=True)

    class Meta:

        model = Trial
        fields = ['trialDbId', 'trialName', 'programDbId', 'name', 'startDate', 'endDate', 'active', 'studies']

    # end class Meta

# end class TrialSerializer
