from django.db import models
from rest_framework import serializers

from brapi.serializers import StringListField


class GAList(models.Model):

    attributeCategoryDbId = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default='')

# end class GAList


class GAAttrAvail(models.Model):

    attributeCategoryDbId = models.IntegerField()
    code = models.CharField(max_length=100, blank=True, default='')
    uri = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    datatype = models.CharField(max_length=100, blank=True, default='')
    values = models.CharField(max_length=100, blank=True, default='')

    def save(self, *args, **kwargs):

        self.values = '; '.join(self.values)
        super(GAAttrAvail, self).save(*args, **kwargs)

    # end def save

# end class GAAttrAvail


class GermplasmAttr(models.Model):

    # TODO: this should be a foreign key
    germplasmDbId = models.CharField(max_length=100, blank=True, default='')
    attributeDbId = models.CharField(max_length=100, blank=True, default='')
    attributeName = models.CharField(max_length=100, blank=True, default='')
    attributeCode = models.CharField(max_length=100, blank=True, default='')
    value = models.CharField(max_length=100, blank=True, default='')
    dateDetermined = models.DateField()

# end class GermplasmAttr


class GAListSerializer(serializers.ModelSerializer):

    class Meta:

        model = GAList
        exclude = ['id']

    # end class Meta

# end class GAListSerializer


class GAAttrAvailSerializer(serializers.ModelSerializer):

    values = StringListField()

    class Meta:

        model = GAAttrAvail
        fields = ['attributeCategoryDbId', 'code', 'uri', 'name', 'description', 'datatype', 'values']

    # end class Meta

    def to_representation(self, instance: GAAttrAvail):

        instance.values = [str(s) for s in instance.values.split('; ')]

        return super(GAAttrAvailSerializer, self).to_representation(instance)

    # end def to_representation


    def to_internal_value(self, data):

        ret = super(GAAttrAvailSerializer, self).to_internal_value(data)

        if ret['values']:
            ret['values'] = '; '.join(str(s) for s in ret['values'])
        # end if

        return ret

    # end def to_internal_value

# end class GAAttrAvailSerializer


class GermplasmAttrSerializer(serializers.ModelSerializer):

    class Meta:

        model = GermplasmAttr
        fields = ['attributeDbId', 'attributeName', 'attributeCode', 'value', 'dateDetermined']

    # end class Meta

# end class GermplasmAttrSerializer
