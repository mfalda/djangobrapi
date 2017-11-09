from django.db import models
from rest_framework import serializers


class Program(models.Model):

    programDbId = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default='')
    abbreviation = models.CharField(max_length=100, blank=True, default='')
    objective = models.CharField(max_length=100, blank=True, default='')
    leadPerson = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Program
    

class ProgramSerializer(serializers.ModelSerializer):

    class Meta:

        model = Program
        exclude = ['id']

    # end class Meta

# end class ProgramSerializer

