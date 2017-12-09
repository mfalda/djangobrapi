from django.db import models
from rest_framework import serializers


class Taxon(models.Model):

    taxonDbId = models.IntegerField(primary_key=True)
    sourceName = models.CharField(max_length=100, blank=True, default='')
    taxonId = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('taxonDbId',)
        
    # end class Meta
    
# end class Taxon


class TaxonSerializer(serializers.ModelSerializer):

    class Meta:

        model = Taxon
        exclude = ['taxonDbId']

    # end class Meta

# end class TaxonSerializer
