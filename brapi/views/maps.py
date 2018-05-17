from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import Q
import logging

from brapi.models import Map, MapLinkage

from brapi.serializers import (MapSerializer, MapDetailSerializer,
                               MapLinkageSerializer, MapLinkagePositionsSerializer)
from brapi.aux_fun import search_get_qparams, paginate
from brapi.paginators import BrAPISimplePagination


class MapView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Map.objects.all()
        queryset = search_get_qparams(self, queryset, [('type', 'type'), ('species', 'species')])

        return paginate(queryset, request, MapSerializer)
    
    # end def get
    
# end class MapView
    
    
class MapDetailView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        
        mapDbId = self.kwargs['mapDbId']
        
        queryset = Map.objects.all()
        queryset = queryset.filter(mapDbId=mapDbId)

        return paginate(queryset, request, MapDetailSerializer, BrAPISimplePagination)
    
    # end def get
    
# end class MapDetailView
    
    
class MapLinkageView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)

        mapDbId = self.kwargs['mapDbId']
        queryset = MapLinkage.objects.all()

        linkageGroupId = self.request.query_params.get('linkageGroupId', None)
        logger.warning("Linkages: (%s, %s)" % (mapDbId, linkageGroupId))

        queryset = search_get_qparams(self, queryset, [('mapDbId', 'mapDbId'), ('linkageGroupId', 'linkageGroupId')])

        return paginate(queryset, request, MapLinkageSerializer)
    
    # end def get
    
# end class MapLinkageView


# cannot use ViewSets nor generic views because the detail view is not standard
class MapLinkageViewPositions(APIView):

    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)

        mapDbId = self.kwargs['mapDbId']
        queryset = MapLinkage.objects.all()

        linkageGroupId = self.kwargs['linkageGroupId']
        logger.warning("Positions: (%s, %s)" % (mapDbId, linkageGroupId))

        queryset = queryset.filter(Q(mapDbId=mapDbId)&Q(linkageGroupId=linkageGroupId))

        # numerical filters, therefore cannot use '_search_get_qparams'
        min_pos = self.request.query_params.get('min', None)
        if min_pos is not None:
            queryset = queryset.filter(location__gte=min_pos)
        # end if

        max_pos = self.request.query_params.get('max', None)
        if max_pos is not None:
            queryset = queryset.filter(location__lte=max_pos)
        # end if

        return paginate(queryset, request, MapLinkagePositionsSerializer)
      
    # end def get

# end class MapLinkageViewPositions
