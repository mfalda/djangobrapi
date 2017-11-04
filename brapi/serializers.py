from rest_framework import serializers


class StringListField(serializers.ListField):

    child = serializers.CharField(max_length=10, default='GET')

 # end class StringListField
