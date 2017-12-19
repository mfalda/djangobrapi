from rest_framework.views import APIView
import logging

from brapi.models import ObservationVariable, ObservationVariableDatatype, Ontology
from brapi.serializers import (ObservationVariableSerializer, OntologySerializer,
                               ObservationVariableDatatypeSerializer)

from brapi.aux_fun import paginate, search_post_params_in

from brapi.paginators import BrAPIListPagination


class ObservationVariableDatatypeView(APIView):
    
    def get(self, request, format=None, *args, **kwargs):

        queryset = ObservationVariableDatatype.objects.all()

        return paginate(queryset, request, ObservationVariableDatatypeSerializer, BrAPIListPagination)

    # end def get

# end class ObservationVariableDatatypeView


class OntologyView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Ontology.objects.all()

        return paginate(queryset, request, OntologySerializer)

    # end def get

# end class OntologyView
    
    
class ObservationVariableView(APIView):
    
    serializer_class = ObservationVariableSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = ObservationVariable.objects.all()

        observationVariableDbId = self.kwargs.get('observationVariableDbId', None)
        if observationVariableDbId is not None:
            queryset = queryset.filter(observationVariableDbId=observationVariableDbId)
        # end if

        return paginate(queryset, request, ObservationVariableSerializer)

    # end def get_queryset

# end class ObservationVariableView


class ObservationVariablesListView(APIView):
    
    serializer_class = ObservationVariableSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = ObservationVariable.objects.all()

        # this search is not standard since it is on a related table
        param_value = self.request.query_params.get('traitClass', None)
        if param_value is not None:
            queryset = queryset.filter(traitDbId__classis=param_value)
        # end if

        return paginate(queryset, request, ObservationVariableSerializer)

    # end def get

# end class ObservationVariablesListView


class ObservationVariableSearchView(APIView):

    serializer_class = ObservationVariableSerializer

    def post(self, request, format=None, *args, **kwargs):

        # PARAMS:
        # {
        #     "page": 0,
        #     "pageSize": 2,
        #     "observationVariableDbIds" : ["obs-variable-id1", "obs-variable-id1"],
        #     "ontologyXrefs" : ["CO:123", "CO:456"],
        #     "ontologyDbIds" : ["CO_334:0100632"],
        #     "methodDbIds" : ["method-1", "method=2"],
        #     "scaleDbIds" : ["scale-1", "scale-2"],
        #     "names" : ["caro_spectro"],
        #     "datatypes" : ["numeric"],
        #     "traitClasses" : ["Phenological", "Physiological"]
        # }

        params = self.request.data
        
        logger = logging.getLogger(__name__)
        logger.warning("Search parameters: %s" % params)
        
        queryset = ObservationVariable.objects.all()

        # TODO: add ('datatypes'), ('traitClasses')
        queryset = search_post_params_in(self, queryset, [
            ('observationVariableDbIds', 'observationVariableDbId'),
            ('ontologyXrefs', 'xref'),
            ('ontologyDbIds', 'ontologyDbId'),
            ('methodDbIds', 'methodDbId__methodDbId'),
            ('scaleDbIds', 'scales__scaleDbId'),
            ('names', 'observationVariableName'),
            ('datatypes', 'scales__datatypeDbId__data'),
            ('traitClasses', 'traitDbId__classis')])

        return paginate(queryset, request, ObservationVariableSerializer)

    # end def post

# end class ObservationVariableSearchView
