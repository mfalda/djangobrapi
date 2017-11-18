from django.db import models
from rest_framework import serializers

from brapi.aux_types import StringListField


class Trait(models.Model):

    traitDbId = models.IntegerField()
    traitId = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    observationVariables = models.CharField(max_length=100, blank=True, default='')
    _defaultValue = models.IntegerField(null=True)

    def save(self, *args, **kwargs):

        self.observationVariables = '; '.join(self.observationVariables)
        super(Trait, self).save(*args, **kwargs)

    # end def save


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
    
    def get_defaultValue(self):
        
        return self._defaultValue if self._defaultValue is not None else 'NA'
    
    # end def get_defaultValue
    
    defaultValue = property(get_defaultValue)
    
# end class Trait




class TraitSerializer(serializers.ModelSerializer):

    observationVariables = StringListField()

    class Meta:

        model = Trait
        fields = ['traitDbId', 'traitId', 'name', 'description', 'observationVariables', 'defaultValue']

    # end class Meta


    def to_representation(self, instance: Trait):

        instance.observationVariables = [str(s) for s in instance.observationVariables.split('; ')]

        return super(TraitSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(TraitSerializer, self).to_internal_value(data)

        if ret['observationVariables']:
            ret['observationVariables'] = '; '.join(str(s) for s in ret['observationVariables'])
        # end if

        return ret

    # end def to_internal_value

# end class TraitSerializer
