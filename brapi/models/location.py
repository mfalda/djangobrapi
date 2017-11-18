from django.db import models
from rest_framework import serializers
import logging

from brapi.aux_types import StringDictField
from brapi.serializers import ExtendedSerializer


class Location(models.Model):

    locationDbId = models.IntegerField()
    locationType = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    abbreviation = models.CharField(max_length=100, blank=True, default='')
    countryCode = models.CharField(max_length=100, blank=True, default='')
    countryName = models.CharField(max_length=100, blank=True, default='')
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.CharField(max_length=100, blank=True, default='')
    instituteName = models.CharField(max_length=100, blank=True, default='')
    instituteAdress = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Location


class LocationAdditionalInfo(models.Model):

    locationdbid = models.OneToOneField(Location, models.DO_NOTHING, 
                                     related_name='additionalInfo', 
                                     db_column='locationDbId', 
                                     blank=True, null=True)
    values = models.CharField(max_length=100, blank=True, default='')

    class Meta:

        ordering = ('id',)

	# end class Meta
    
# end class LocationAdditionalInfo


class LocationAdditionalInfoSerializer(serializers.ModelSerializer):

    values = StringDictField()
    
    class Meta:

        model = LocationAdditionalInfo
        exclude = ['id', 'locationdbid']

    # end class Meta
    

    def to_representation(self, instance: LocationAdditionalInfo):
        
        instance.values = {l.split(':')[0]: l.split(':')[1] for l in instance.values.split('; ')}
        logger = logging.getLogger(__name__)
        logger.warn("Splitting %s" % instance.values)

        return super(LocationAdditionalInfoSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, values):

        ret = super(LocationAdditionalInfoSerializer, self).to_internal_value(values)

        if ret['values']:
            ret['values'] = '; '.join(['%s:%s' % (k, v) for (k, v) in ret['values']])
        # end if

        return ret

    # end def to_internal_value
    
# end class LocationAdditionalInfoSerializer
    
    
class LocationSerializer(ExtendedSerializer):

    additionalInfo = LocationAdditionalInfoSerializer(many=False, read_only=True)

    class Meta:

        model = Location
        fields = '__all__'
        excluded = ['id']
        extra_fields = ['additionalInfo']

    # end class Meta

# end class LocationSerializer
