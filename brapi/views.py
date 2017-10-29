from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from brapi.apps import BrAPIResultsSetPagination, BrAPIListPagination
from rest_framework.views import APIView
from django.db.models import Q
import logging

from brapi.models import Call, Trait, Crop, Program, Map, MapLinkage, Marker, Trait
from brapi.serializers import (CallsSerializer, LocationSerializer, CropSerializer, 
    ProgramSerializer, MapSerializer, MapLinkageSerializer, MarkerSerializer, TraitSerializer)
    

# the DefaultRouter class we're using in urls.py  also automatically creates the API root view


def _search_params(self, queryset, params):

    #  [('name', 'name'), ('type', 'type'), ('matchMethod', 'matchMethod'), ('include', 'synonyms')]
    for (param_name, search) in params:
        param_value = self.request.query_params.get(param_name, None)
        if param_value is not None:
            queryset = queryset.filter(**{search: param_value})
        # end if
    # end for

    return queryset

# end def _search_params


class CallsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = Call.objects.all()
    serializer_class = CallsSerializer
    paginate_by_param = 'pageSize'

# end class CallsViewSet


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProgramSerializer
    paginate_by_param = 'pageSize'

    def get_queryset(self):

        queryset = Program.objects.all()

        return _search_params(self, queryset, [('programName', 'programName'), ('abbreviation', 'abbreviation')])
    
    # end def get_queryset

# end class ProgramViewSet


class CropViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CropSerializer
    paginate_by_param = 'pageSize'
    pagination_class = BrAPIListPagination
    queryset = Crop.objects.all()

# end class CropViewSet


class MapViewSet(viewsets.ReadOnlyModelViewSet):
   
    paginate_by_param = 'pageSize'
     
    def get_queryset(self):

        self.serializer_class = MapSerializer
        queryset = Map.objects.all()

        return _search_params(self, queryset, [('type', 'type'), ('species', 'species')])
    
    # end def get_queryset

# end class MapViewSet


class MapLinkageView(generics.ListCreateAPIView):
   
    paginate_by_param = 'pageSize'
    serializer_class = MapLinkageSerializer

    def get_queryset(self):

        logger = logging.getLogger(__name__)
        
        mapDbId = self.kwargs['mapDbId']
        queryset = MapLinkage.objects.all()
                
        linkageGroupId = self.request.query_params.get('linkageGroupId', None)
        logger.warn("Linkages: (%s, %s)" % (mapDbId, linkageGroupId))

        queryset = queryset.filter(mapDbId=mapDbId)

        return _search_params(self, queryset, [('linkageGroupId', 'linkageGroupId')])
    
    # end def get_queryset

# end class MapLinkageView


# cannot use ViewSets nor generic views because the detail view is not standard
class MapLinkageViewPositions(APIView):
   
    paginate_by_param = 'pageSize'

    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)
        
        mapDbId = self.kwargs['mapDbId']
        queryset = MapLinkage.objects.all()
        
        linkageGroupId = self.kwargs['linkageGroupId']
        logger.warn("Positions: (%s, %s)" % (mapDbId, linkageGroupId))

        queryset = queryset.filter(Q(mapDbId=mapDbId)&Q(linkageGroupId=linkageGroupId))

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


# cannot use ViewSets because the previous detail view is not standard
class LocationViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = LocationSerializer
    paginate_by_param = 'pageSize'

    def get_queryset(self):
        """
        Optionally restricts the returned records
        """

        queryset = Location.objects.all()

        location_type = self.request.query_params.get('locationType', None)
        if location_type is not None:
            queryset = queryset.filter(locationType=location_type)
        # end if
        
        return queryset
    
    # end def get_queryset

# end class LocationViewSet


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = MarkerSerializer
    paginate_by_param = 'pageSize'

    def get_queryset(self):

        queryset = Marker.objects.all()

        # name, matchMethod, include
        # possible values are 'case_insensitive', 'exact' (case sensitive), 'wildcard' (which is case insensitive). Wildcard uses both '*' and '%' for any number of characters and '?' for one character matching. Default is exact.
        # Whether to include synonyms in the output.
        name = self.request.query_params.get('name', None)
        match_method = self.request.query_params.get('matchMethod', None)
        include = self.request.query_params.get('include', None)

        synonyms = include is not None and include == 'synonyms'

        logger = logging.getLogger(__name__)
        logger.warn("FILTERING: %s, method=%s, synonyms=%s" % (name, match_method, synonyms))

        if name is not None:
            if match_method is not None:
                if match_method == 'case_insensitive':
                    if synonyms:
                        queryset = queryset.filter(Q(defaultDisplaydefaultDisplayName__iexact=name)|Q(synonyms__iexact=name))
                    else:
                        queryset = queryset.filter(defaultDisplayName__iexact=name)
                    # end if
                elif match_method == 'wildcard':
                    # TODO: add prefixes and suffixes
                    name = name.replace('*', '')
                    name = name.replace('%', '')
                    if synonyms:
                        queryset = queryset.filter(Q(defaultDisplayName__icontains=name)|Q(synonyms__contains=name))
                    else:
                        queryset = queryset.filter(defaultDisplayName__icontains=name)
                    # end if
                # end if
            else: # exact
                if synonyms:
                    queryset = queryset.filter(Q(defaultDisplayName=name)|Q(synonyms=name))
                else:
                    queryset = queryset.filter(defaultDisplayName=name)
                # end if
            # end if
        # end if

        # the type of the marker.
        type = self.request.query_params.get('type', None)
        if type is not None:
            queryset = queryset.filter(type=type)
        # end if

        return queryset
    
    # end def get_queryset

# end class MarkerViewSet


class TraitViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TraitSerializer
    paginate_by_param = 'pageSize'
    queryset = Trait.objects.all()

# end class TraitViewSet