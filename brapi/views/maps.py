from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from django.db.models import Q
import logging

from brapi.models.map import Map, MapLinkage, MapSerializer, MapLinkageSerializer

from brapi.aux_fun import _search_get_qparams


class MapViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):

        self.serializer_class = MapSerializer
        queryset = Map.objects.all()

        return _search_get_qparams(self, queryset, [('type', 'type'), ('species', 'species')])

    # end def get_queryset

# end class MapViewSet


class MapLinkageView(generics.ListCreateAPIView):

    serializer_class = MapLinkageSerializer

    def get_queryset(self):

        logger = logging.getLogger(__name__)

        mapDbId = self.kwargs['mapDbId']
        queryset = MapLinkage.objects.all()

        linkageGroupId = self.request.query_params.get('linkageGroupId', None)
        logger.warn("Linkages: (%s, %s)" % (mapDbId, linkageGroupId))

        return _search_get_qparams(self, queryset, [('mapDbId', 'mapDbId'), ('linkageGroupId', 'linkageGroupId')])

    # end def get_queryset

# end class MapLinkageView


# cannot use ViewSets nor generic views because the detail view is not standard
class MapLinkageViewPositions(APIView):

    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)

        mapDbId = self.kwargs['mapDbId']
        queryset = MapLinkage.objects.all()

        linkageGroupId = self.kwargs['linkageGroupId']
        logger.warn("Positions: (%s, %s)" % (mapDbId, linkageGroupId))

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

        serializer = MapLinkageSerializer(queryset, many=True)

        return Response(serializer.data)           

    # end def get

# end class MapLinkageViewPositions