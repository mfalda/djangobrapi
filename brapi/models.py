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

