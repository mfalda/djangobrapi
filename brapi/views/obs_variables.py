from rest_framework import viewsets
from rest_framework.views import APIView
import logging

from brapi.models import ObservationVariable, ObservationVariableDatatype, Ontology
from brapi.serializers import (ObservationVariableSerializer, OntologySerializer,
                               ObservationVariableDatatypeSerializer)

from brapi.aux_fun import paginate, search_post_params_in

from brapi.paginators import BrAPIListPagination


class ObservationVariableDatatypeViewSet(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = ObservationVariableDatatypeSerializer
    pagination_class = BrAPIListPagination
    queryset = ObservationVariableDatatype.objects.all()

# end class ObservationVariableDatatypeViewSet


class OntologiesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Ontology.objects.all()
    serializer_class = OntologySerializer

# end class OntologiesViewSet
    
    
class ObsVariablesView(APIView):
    
    serializer_class = ObservationVariableSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = ObservationVariable.objects.all()

        observationVariableDbId = self.kwargs.get('observationVariableDbId', None)
        if observationVariableDbId is not None:
            queryset = queryset.filter(observationVariableDbId=observationVariableDbId)
        # end if

        return paginate(queryset, request, ObservationVariableSerializer)

    # end def get_queryset

# end class ObsVariablesView


class ObsVariablesListView(APIView):
    
    serializer_class = ObservationVariableSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = ObservationVariable.objects.all()

        # this search is not standard since it is on a related table
        param_value = self.request.query_params.get('traitClass', None)
        if param_value is not None:
            queryset = queryset.filter(trait__classe=param_value)
        # end if

        return paginate(queryset, request, ObservationVariableSerializer)

    # end def get

# end class ObsVariablesListView


class VSearchView(APIView):

    serializer_class = ObservationVariableSerializer

    def post(self, request, format=None, *args, **kwargs):

        params = self.request.data
        
        logger = logging.getLogger(__name__)
        logger.warning("Search parameters: %s" % params)
        
        queryset = ObservationVariable.objects.all()

        # TODO: add ('datatypes'), ('traitClasses')
        queryset = search_post_params_in(self, queryset, [('observationVariableDbId', 'observationVariableDbIds'),
            ('ontologyXref', 'ontologyXrefs'),
            ('ontologyDbId', 'ontologyDbIds'),
            ('method', 'methodDbIds'),
            ('scale', 'scaleDbIds'),
            ('name', 'names')])

        return paginate(queryset, request, ObservationVariableSerializer)

    # end def post

# end class VSearchView
