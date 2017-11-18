from django.db import models
from rest_framework import serializers


class Map(models.Model):

    mapDbId = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, blank=True, default='')
    species = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='')
    unit = models.CharField(max_length=100, blank=True, default='')
    publishedDate = models.DateField()
    markerCount = models.IntegerField()
    comments = models.CharField(max_length=100, blank=True, default='')


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class Map
  
    
class MapLinkage(models.Model):

    mapDbId = models.ForeignKey(Map, db_column='mapDbId', related_name='linkageGroups', on_delete=models.CASCADE, default='', to_field='mapDbId')
    markerDbId = models.IntegerField()
    markerName = models.CharField(max_length=100, blank=True, default='')
    location = models.IntegerField()
    linkageGroupId = models.IntegerField()


    class Meta:
        
        ordering = ('id',)
        
    # end class Meta
    
# end class MapLinkage


class MapLinkageSerializer(serializers.ModelSerializer):

    class Meta:

        model = MapLinkage
        exclude = ['id', 'mapDbId']

    # end class Meta

# end class MapLinkageSerializer


class MapSerializer(serializers.ModelSerializer):

    linkageGroupCount = serializers.SerializerMethodField()
    
    
    class Meta:

        model = Map
        fields = ['mapDbId', 'name', 'species', 'type', 'unit', 'publishedDate', 
                    'markerCount', 'comments', 'linkageGroupCount']

    # end class Meta


    def get_linkageGroupCount(self, obj):
        
        return obj.linkageGroups.count()
    
    # end def get_linkageGroupCount
    
# end class MapSerializer


class MapDetailSerializer(serializers.ModelSerializer):

    linkageGroups = MapLinkageSerializer(many=True, read_only=True)
    

    class Meta:

        model = Map
        fields = ['mapDbId', 'name', 'species', 'type', 'unit', 'publishedDate', 
                    'markerCount', 'comments', 'linkageGroups']

    # end class Meta

# end class MapDetailSerializer
    