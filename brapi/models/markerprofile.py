from django.db import models
from rest_framework import serializers

from brapi.models.germplasm import Germplasm
from brapi.aux_types import StringListField, IntListField
from brapi.serializers import ExtendedSerializer


class AlleleMatrix(models.Model):
    
    name = models.CharField(max_length=100, blank=True, default='')
    matrixDbId = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, default='')
    lastUpdated = models.DateField()
    studyDbId = models.IntegerField()


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class AlleleMatrix


class AlleleMSearch(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
    
        self.data = '; '.join(self.data)

    # end def save
    

    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class AlleleMSearch

    
class MarkerProfile(models.Model):

    germplasmDbId = models.IntegerField()
        # TODO: models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='mprofiles-details+', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    markerprofileDbId = models.IntegerField(primary_key=True)
    uniqueDisplayName = models.CharField(max_length=100, blank=True, default='')
    sampleDbId = models.IntegerField()
    extractDbId = models.IntegerField()
    studyDbId = models.IntegerField()
    analysisMethod = models.CharField(max_length=100, blank=True, default='')
    resultCount = models.IntegerField()


    class Meta:
        
        ordering = ('markerprofileDbId',)
        
    # end class Meta
    
# end class MarkerProfile
    

class GermplasmMarkerprofile(models.Model):

    germplasmDbId = models.IntegerField()
        # TODO: models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='germplasmDbId_details', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    markerprofilesDbIds = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta


    def save(self, *args, **kwargs):

        self.markerprofilesDbIds = '; '.join(self.markerprofilesDbIds)

    # end def save

# end class GermplasmMarkerprofile
    
    
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


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
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

    def to_representation(self, instance):
        
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
    
    
class GermplasmMarkerprofileSerializer(serializers.ModelSerializer):

    markerprofilesDbIds = IntListField()


    class Meta:

        model = GermplasmMarkerprofile
        fields = ['germplasmDbId', 'markerprofilesDbIds']

    # end class Meta


    def to_representation(self, instance):

        instance.markerprofilesDbIds = [str(s) for s in instance.markerprofilesDbIds.split('; ')]

        return super(GermplasmMarkerprofileSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(GermplasmMarkerprofileSerializer, self).to_internal_value(data)

        if ret['markerprofilesDbIds']:
            ret['markerprofilesDbIds'] = '; '.join(str(s) for s in ret['markerprofilesDbIds'])
        # end if

        return ret

    # end def to_internal_value

# end class GermplasmMarkerprofile
    
    
class MarkerProfileSerializer(ExtendedSerializer):

    markerprofilesDbIds = GermplasmMarkerprofileSerializer(many=True, read_only=True)
    
    class Meta:

        model = MarkerProfile
        fields = ['germplasmDbId', 'markerprofilesDbIds']

    # end class Meta

# end class MarkerProfileSerializer


class MarkerProfilesDataSerializer(serializers.ModelSerializer):
    
    data = StringListField()

    class Meta:

        model = MarkerProfilesData
        exclude = ['id']

    # end class Meta

    def to_representation(self, instance):
    
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
    