from django.db import models
from rest_framework import serializers


class Taxon(models.Model):

    ncbiTaxon = models.CharField(max_length=100, blank=True, default='')
    ciradTaxon = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Taxon


class TaxonSerializer(serializers.ModelSerializer):

    class Meta:

        model = Taxon
        exclude = ['id']

    # end class Meta

# end class TaxonSerializer
    