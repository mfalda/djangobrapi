from rest_framework import viewsets
import logging
from django.db.models import Q

from brapi.models.marker import Marker, MarkerSerializer

from brapi.aux_fun import search_get_qparams


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = MarkerSerializer

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

        return search_get_qparams(self, queryset, [('type', 'type')])

    # end def get_queryset

# end class MarkerViewSet
    