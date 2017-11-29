from django.db import models
from rest_framework import serializers

from brapi.models.observation import (ObsMethodSerializer, ObsTraitSerializer,
                                      ObsScaleSerializer)

from brapi.aux_types import StringListField, StringDictField
from brapi.serializers import ExtendedSerializer



class Trial(models.Model):

    trialDbId = models.IntegerField(unique=True)
    trialName = models.CharField(max_length=100, blank=True, default='')
    programDbId = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default='')
    startDate = models.DateField()
    endDate = models.DateField()
    active = models.BooleanField()


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Trial
    
    
class TrialAdditionalInfo(models.Model):

    trialdbid = models.OneToOneField(Trial, models.DO_NOTHING, 
                                     related_name='additionalInfo', 
                                     db_column='trialDbId', 
                                     blank=True, null=True)
    values = models.CharField(max_length=100, blank=True, default='')

    class Meta:

        ordering = ('id',)

	# end class Meta
    
# end class TrialAdditionalInfo
    
    
class Treatment(models.Model):

    treatmentId = models.IntegerField()
    factor = models.CharField(max_length=100, blank=True, default='')
    modality = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Treatment


class DataLink(models.Model):

    type = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    url = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class DataLink
    
    
class StudySeason(models.Model):
    
    seasonDbId = models.IntegerField(primary_key=True, db_column='id')
    season = models.CharField(max_length=100, blank=True, default='')
    year = models.IntegerField()


    class Meta:
        
        ordering = ('seasonDbId',)
        
    # end class Meta
    
# end class StudySeason


class StudyType(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class StudyType


class StudyObsLevel(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
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


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class StudyPlot


class StudyPlotAdditionalInfo(models.Model):

    studyDbId = models.OneToOneField(StudyPlot, models.DO_NOTHING, 
                                     related_name='additionalInfo', 
                                     db_column='studyDbId', 
                                     blank=True, null=True)
    values = models.CharField(max_length=100, blank=True, default='')

    class Meta:

        ordering = ('id',)

	# end class Meta
    
# end class StudyPlotAdditionalInfo


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
    lastUpdate = models.CharField(max_length=100, null=True, default='')

    def save(self, *args, **kwargs):

        if self.seasons:
            self.seasons = '; '.join(self.seasons)
        # end if
        
        if self.contactDbId:
            self.contactDbId = '; '.join(self.contactDbId)
        # end if

    # end def save
    

    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
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
    

    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
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


class StudyPlotAdditionalInfoSerializer(serializers.ModelSerializer):

    values = StringDictField()
    
    
    class Meta:

        model = StudyPlotAdditionalInfo
        exclude = ['id', 'studyDbId']

    # end class Meta
    

    def to_representation(self, instance: StudyPlotAdditionalInfo):
        
        if instance.values != '':
            instance.values = {l.split(':')[0]: l.split(':')[1] for l in instance.values.split('; ')}
        else:
            instance.values = {}            
        # end if
        
        return super(StudyPlotAdditionalInfoSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, values):

        ret = super(StudyPlotAdditionalInfoSerializer, self).to_internal_value(values)

        if ret['values']:
            ret['values'] = '; '.join(['%s:%s' % (k, v) for (k, v) in ret['values']])
        # end if

        return ret

    # end def to_internal_value
    
# end class StudyPlotAdditionalInfoSerializer
    
    
class StudyPlotSerializer(ExtendedSerializer):

    additionalInfo = StudyPlotAdditionalInfoSerializer(many=False, read_only=True)
    
    class Meta:

        model = StudyPlot
        fields = '__all__'
        excluded = ['id']
        extra_fields = ['additionalInfo']

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

    #seasons = StringListField()
    #contactDbId = StringListField()
    
    class Meta:

        model = Study
        fields = ['studyDbId', 'studyName', 'locationName', 'locationDbId']
        
    # end class Meta


    def to_representation(self, instance: Study):
    
        if instance.seasons:
            instance.seasons = [str(s) for s in instance.seasons.split('; ')]
        # end if
        
        if instance.contactDbId:
            instance.contactDbId = [str(s) for s in instance.contactDbId.split('; ')]
        # end if
            
        return super(StudySerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(StudySerializer, self).to_internal_value(data)

        if ret['seasons']:
            ret['seasons'] = '; '.join(str(s) for s in ret['seasons'])
        # end if
        
        if ret['contactDbId']:
            ret['contactDbId'] = '; '.join(str(s) for s in ret['contactDbId'])
        # end if

        return ret

    # end def to_internal_value
    
# end class StudySerializer


class TrialAdditionalInfoSerializer(serializers.ModelSerializer):

    values = StringDictField()
    
    class Meta:

        model = TrialAdditionalInfo
        exclude = ['id', 'trialdbid']

    # end class Meta
    

    def to_representation(self, instance: TrialAdditionalInfo):
        
        if instance.values != '':
            instance.values = {l.split(':')[0]: l.split(':')[1] for l in instance.values.split('; ')}
        else:
            instance.values = {}
        # end if

        return super(TrialAdditionalInfoSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, values):

        ret = super(TrialAdditionalInfoSerializer, self).to_internal_value(values)

        if ret['values']:
            ret['values'] = '; '.join(['%s:%s' % (k, v) for (k, v) in ret['values']])
        # end if

        return ret

    # end def to_internal_value
    
# end class TrialAdditionalInfoSerialize
    
    
class TrialSerializer(ExtendedSerializer):

    studies = StudySerializer(many=True, read_only=True)
    additionalInfo = TrialAdditionalInfoSerializer(many=False, read_only=True)

    class Meta:

        model = Trial
        fields = '__all__'
        excluded = ['id']
        extra_fields = ['studies', 'additionalInfo']
        
    # end class Meta

# end class TrialSerializer
