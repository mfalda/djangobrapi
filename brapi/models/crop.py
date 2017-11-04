from django.db import models
from rest_framework import serializers


class Crop(models.Model):

    data = models.CharField(max_length=100, blank=True, default='')

# end class Crop


class CropSerializer(serializers.ModelSerializer):

    class Meta:

        model = Crop
        fields = ['data']

    # end class Meta

# end class CropSerializer
    