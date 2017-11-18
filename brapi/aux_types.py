from rest_framework import serializers
from enum import Enum


class IntListField(serializers.ListField):

    child = serializers.IntegerField()

 # end class StringListField
 

class StringListField(serializers.ListField):

    child = serializers.CharField(max_length=10, default='GET')

 # end class StringListField


class StringDictField(serializers.DictField):

    child = serializers.CharField(max_length=10, default='GET')

 # end class StringDictField


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)
    # end def choices

# end class ChoiceEnum


class SeasonType(ChoiceEnum):

    SPRING = 'Spring'
    SUMMER = 'Summer'
    AUTUMN = 'Autumn'
    WINTER = 'Winter'

# end class SeasonType
