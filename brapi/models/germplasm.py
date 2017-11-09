from django.db import models
from rest_framework import serializers

from brapi.models.taxon import Taxon, TaxonSerializer
from brapi.serializers import StringListField


class Germplasm(models.Model):

    germplasmDbId = models.IntegerField(unique=True)
    defaultDisplayName = models.CharField(max_length=100, blank=True, default='')
    accessionNumber = models.CharField(max_length=100, blank=True, default='')
    germplasmName = models.CharField(max_length=100, blank=True, default='')
    germplasmPUI = models.CharField(max_length=100, blank=True, default='')
    pedigree = models.CharField(max_length=100, blank=True, default='')
    germplasmSeedSource = models.CharField(max_length=100, blank=True, default='')
    synonyms = models.CharField(max_length=100, blank=True, default='')
    commonCropName = models.CharField(max_length=100, blank=True, default='')
    instituteCode = models.CharField(max_length=100, blank=True, default='')
    instituteName = models.CharField(max_length=100, blank=True, default='')
    biologicalStatusOfAccessionCode = models.IntegerField()
    countryOfOriginCode = models.CharField(max_length=100, blank=True, default='')
    typeOfGermplasmStorageCode = models.CharField(max_length=100, blank=True, default='')
    genus = models.CharField(max_length=100, blank=True, default='')
    species = models.CharField(max_length=100, blank=True, default='')
    speciesAuthority = models.CharField(max_length=100, blank=True, default='')
    subtaxa = models.CharField(max_length=100, blank=True, default='')
    subtaxaAuthority = models.CharField(max_length=100, blank=True, default='')
    # TODO: this should be a FK, but it is a circular constraint!
    donors = models.CharField(max_length=100, blank=True, default='')
    acquisitionDate = models.DateField()
    # TODO: represent as a list of objects
    taxonIds = models.ForeignKey(Taxon, db_column='taxonIds', related_name='taxonIds', on_delete=models.CASCADE, default='', to_field='id')

    def save(self, *args, **kwargs):

        self.synonyms = '; '.join(self.synonyms)
        self.taxonIds = '; '.join(self.taxonIds)
        self.donors = '; '.join(self.donors)
        super(Germplasm, self).save(*args, **kwargs)

    # end def save


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Germplasm


class GPPedigree(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='gppedigrees-details+', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    defaultDisplayName = models.CharField(max_length=100, blank=True, default='')
    pedigree = models.CharField(max_length=100, blank=True, default='')
    # TODO: is this a foreign key?
    parent1Id = models.IntegerField()
    # TODO: is this a foreign key?
    parent2Id = models.IntegerField()


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class GPPedigree


class GPDonor(models.Model):

    germplasmDbId = models.ForeignKey(Germplasm, db_column='germplasmDbId', related_name='gpdonors-details+', on_delete=models.CASCADE, default='', to_field='germplasmDbId')
    donorAccessionNumber = models.CharField(max_length=100, blank=True, default='')
    donorInstituteCode = models.CharField(max_length=100, blank=True, default='')
    germplasmPUI = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class GPDonor
  
    
class GermplasmSerializer(serializers.ModelSerializer):

    synonyms = StringListField()
    donors = StringListField()
    taxonIds = TaxonSerializer(read_only=True)
    
    class Meta:

        model = Germplasm
        fields = ['germplasmDbId', 'defaultDisplayName', 'accessionNumber', 
                  'germplasmName', 'germplasmPUI', 'pedigree', 'germplasmSeedSource', 
                  'synonyms', 'commonCropName', 'instituteCode', 'instituteName',
                  'biologicalStatusOfAccessionCode', 'countryOfOriginCode', 
                  'typeOfGermplasmStorageCode', 'genus', 'species', 'speciesAuthority',
                  'subtaxa', 'subtaxaAuthority', 'donors', 'acquisitionDate', 
                  'taxonIds']

    # end class Meta


    def to_representation(self, instance: Germplasm):

        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]
        instance.donors = [str(s) for s in instance.donors.split('; ')]

        return super(GermplasmSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(GermplasmSerializer, self).to_internal_value(data)

        if ret['synonyms']:
            ret['synonyms'] = '; '.join(str(s) for s in ret['synonyms'])
        # end if

        if ret['donors']:
            ret['donors'] = '; '.join(str(s) for s in ret['donors'])
        # end if
       
        return ret

    # end def to_internal_value    

# end class GermplasmSerializer


class GPPedigreeSerializer(serializers.ModelSerializer):

    class Meta:

        model = GPPedigree
        fields = ['germplasmDbId', 'defaultDisplayName', 'pedigree', 'parent1Id', 'parent2Id']

    # end class Meta

# end class GPPedigreeSerializer


class GPDonorSerializer(serializers.ModelSerializer):

    germplasmDbId = GermplasmSerializer(many=True, read_only=True)

    class Meta:

        model = GPDonor
        exclude = ['id']

    # end class Meta

# end class GPDonorSerializer
