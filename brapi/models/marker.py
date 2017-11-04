from django.db import models
from rest_framework import serializers

from brapi.serializers import StringListField


class Marker(models.Model):

    markerDbId = models.IntegerField()
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



class MarkerSerializer(serializers.ModelSerializer):

    synonyms = StringListField()   
    refAlt = StringListField()   
    analysisMethods = StringListField()   

    class Meta:

        model = Marker
        fields = ('markerDbId', 'defaultDisplayName', 'type', 'synonyms', 'refAlt', 'analysisMethods')

    # end class Meta


    def to_representation(self, instance: Marker):

        instance.synonyms = [str(s) for s in instance.synonyms.split('; ')]
        instance.refAlt = [str(s) for s in instance.refAlt.split('; ')]
        instance.analysisMethods = [str(s) for s in instance.analysisMethods.split('; ')]

        return super(MarkerSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(MarkerSerializer, self).to_internal_value(data)

        if ret['synonyms']:
            ret['synonyms'] = '; '.join(str(s) for s in ret['synonyms'])
        # end if

        if ret['refAlt']:
            ret['refAlt'] = '; '.join(str(s) for s in ret['refAlt'])
        # end if

        if ret['analysisMethods']:
            ret['analysisMethods'] = '; '.join(str(s) for s in ret['analysisMethods'])
        # end if

        return ret

    # end def to_internal_value

# end class MarkerSerializer
