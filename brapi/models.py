from django.db import models


class Call(models.Model):
    
    call = models.CharField(max_length=100, blank=True, default='')
    datatypes = models.CharField(max_length=100, blank=True, default='')
    methods = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
  
        self.datatypes = '; '.join(self.datatypes)
        self.methods = '; '.join(self.methods)
        super(Call, self).save(*args, **kwargs)

    # end def save

# end class Call


class Program(models.Model):
    
    programDbId = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    abbreviation = models.CharField(max_length=100, blank=True, default='')
    objective = models.CharField(max_length=100, blank=True, default='')
    leadPerson = models.CharField(max_length=100, blank=True, default='')
    
# end class Program


class Crop(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')
    
# end class Crop


class Map(models.Model):
    
    mapDbId = models.CharField(max_length=100, unique=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    species = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='')
    unit = models.CharField(max_length=100, blank=True, default='')
    publishedDate = models.DateField()
    markerCount = models.CharField(max_length=100, blank=True, default='')
    comments = models.CharField(max_length=100, blank=True, default='')

# end class Map


class MapLinkage(models.Model):
    
    mapDbId = models.ForeignKey(Map, db_column='mapDbId', related_name='linkageGroups', on_delete=models.CASCADE, default='', to_field='mapDbId')
    markerDbId = models.CharField(max_length=100, blank=True, default='')
    markerName = models.CharField(max_length=100, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    linkageGroupId = models.CharField(max_length=100, blank=True, default='')
    
# end class MapLinkage


class Location(models.Model):

    locationDbId = models.CharField(max_length=100, blank=True, default='')
    locationType = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    abbreviation = models.CharField(max_length=100, blank=True, default='')
    countryCode = models.CharField(max_length=100, blank=True, default='')
    countryName = models.CharField(max_length=100, blank=True, default='')
    latitude = models.CharField(max_length=100, blank=True, default='')
    longitude = models.CharField(max_length=100, blank=True, default='')
    altitude = models.CharField(max_length=100, blank=True, default='')
    instituteName = models.CharField(max_length=100, blank=True, default='')
    instituteAdress = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
  
        #self.datatypes = '; '.join(self.datatypes)
        #self.methods = '; '.join(self.methods)
        super(Location, self).save(*args, **kwargs)

    # end def save

# end class Location


class Marker(models.Model):
    
    markerDbId = models.CharField(max_length=100, blank=True, default='')
    defaultDisplayName = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='')
    synonyms = models.CharField(max_length=100, blank=True, default='')
    refAlt = models.CharField(max_length=100, blank=True, default='')
    analysisMethods = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
  
        self.synonyms = '; '.join(self.synonyms)
        self.refAlt = '; '.join(self.refAlt)
        self.analysisMethods = '; '.join(self.analysisMethods)
        super(Marker, self).save(*args, **kwargs)

    # end def save
    
# end class Marker


class Trait(models.Model):
    
    traitDbId = models.CharField(max_length=100, blank=True, default='')
    traitId = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    observationVariables = models.CharField(max_length=100, blank=True, default='')
    defaultValue = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
  
        self.observationVariables = '; '.join(self.observationVariables)
        super(Trait, self).save(*args, **kwargs)

    # end def save

# end class Trait
