from rest_framework.views import APIView
from brapi.aux_fun import paginate
import logging
from django.db.models import Q

from brapi.models import Marker
from brapi.serializers import MarkerSerializer
from brapi.aux_fun import search_get_qparams

  
class MarkerView(APIView):

    def get(self, request, format=None, *args, **kwargs):
    
        queryset = Marker.objects.all()

        # name, matchMethod, include
        # possible values are 'case_insensitive', 'exact' (case sensitive), 'wildcard' (which is case insensitive). Wildcard uses both '*' and '%' for any number of characters and '?' for one character matching. Default is exact.
        # Whether to include synonyms in the output.
        name = self.request.query_params.get('name', None)
        match_method = self.request.query_params.get('matchMethod', None)
        include = self.request.query_params.get('include', None)

        synonyms = include is not None and include == 'synonyms'

        logger = logging.getLogger(__name__)
        logger.warning("FILTERING: %s, method=%s, synonyms=%s" % (name, match_method, synonyms))

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
            else:  # exact
                if synonyms:
                    queryset = queryset.filter(Q(defaultDisplayName=name)|Q(synonyms=name))
                else:
                    queryset = queryset.filter(defaultDisplayName=name)
                # end if
            # end if
        # end if

        queryset = search_get_qparams(self, queryset, [('type', 'type')])
    
        return paginate(queryset, request, MarkerSerializer)

    # end def get

# end class MarkerView
    

class MarkerDetailsView(APIView):

    def get(self, request, format=None, *args, **kwargs):
    
        queryset = Marker.objects.all()
        
        markerDbId = self.kwargs.get('markerDbId', None)
        if markerDbId is not None:
            queryset = queryset.filter(markerDbId=markerDbId)
        # end if

        return paginate(queryset, request, MarkerSerializer)

    # end def get

# end class MarkerDetailsView
