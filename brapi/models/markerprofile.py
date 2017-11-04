from django.db import models
from rest_framework import serializers

from brapi.models.germplasm import Germplasm
from brapi.serializers import StringListField


class AlleleMatrix(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='')
    matrixDbId = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, default='')
    lastUpdated = models.DateField()
    studyDbId = models.IntegerField()

# end class AlleleMatrix


class AlleleMSearch(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
    
        self.data = '; '.join(self.data)

    # end def save
    
# end class AlleleMSearch


class MarkerProfile(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='mprofiles-details+', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    markerProfilesDbId = models.IntegerField()
    uniqueDisplayName = models.CharField(max_length=100, blank=True, default='')
    sampleDbId = models.IntegerField()
    extractDbId = models.IntegerField()
    studyDbId = models.IntegerField()
    analysisMethod = models.CharField(max_length=100, blank=True, default='')
    resultCount = models.IntegerField()

# end class MarkerProfile
  
    
class MarkerProfilesData(models.Model):
    
    germplasmDbId = models.IntegerField()
    uniqueDisplayName = models.CharField(max_length=100, blank=True, default='')
    extractDbId = models.IntegerField()
    markerprofileDbId = models.IntegerField()
    analysisMethod = models.CharField(max_length=100, blank=True, default='')
    data = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.data = '; '.join(self.data)

    # end def save

# end class MarkerProfilesData


class AlleleMatrixSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = AlleleMatrix
        exclude = ['id']

    # end class Meta

# end class AlleleMatrixSerializer


class AlleleMSearchSerializer(serializers.ModelSerializer):
    
    data = StringListField()

    class Meta:

        model = AlleleMSearch
        exclude = ['id']

    # end class Meta

    def to_representation(self, instance: AlleleMSearch):
        
        instance.data = [str(s) for s in instance.data.split('; ')]

        return super(AlleleMSearchSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(AlleleMSearchSerializer, self).to_internal_value(data)

        if ret['data']:
            ret['data'] = '; '.join(str(s) for s in ret['data'])
        # end if

        return ret

    # end def to_internal_value

# end class AlleleMSearchSerializer
    
    
class MarkerProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = MarkerProfile
        exclude = ['id']

    # end class Meta

# end class MarkerProfileSerializer


class MarkerProfilesDataSerializer(serializers.ModelSerializer):
    
    data = StringListField()

    class Meta:

        model = MarkerProfilesData
        exclude = ['id']

    # end class Meta

    def to_representation(self, instance: MarkerProfilesData):
    
        instance.data = [str(s) for s in instance.data.split('; ')]

        return super(MarkerProfilesDataSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(MarkerProfilesDataSerializer, self).to_internal_value(data)

        if ret['data']:
            ret['data'] = '; '.join(str(s) for s in ret['data'])
        # end if

        return ret

    # end def to_internal_value
    
# end class MarkerProfilesDataSerializer
    