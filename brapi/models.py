from django.db import models


class Call(models.Model):
    
    call = models.CharField(max_length=100, blank=True, default='')
    datatypes = models.CharField(max_length=100, blank=True, default='')
    methods = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):
  
        #self.datatypes = '; '.join(self.datatypes)
        #self.methods = '; '.join(self.methods)
        super(Call, self).save(*args, **kwargs)

    # end def save

# end class Call


class Crop(models.Model):
    
    data = models.CharField(max_length=100, blank=True, default='')
    
# end class Crop


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