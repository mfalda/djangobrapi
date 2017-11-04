from django.db import models
from rest_framework import serializers


class Location(models.Model):

    locationDbId = models.CharField(max_length=100, blank=True, default='')
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

# end class Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Location
        exclude = ['id']

    # end class Meta

# end class LocationSerializer
    