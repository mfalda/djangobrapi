from rest_framework import viewsets
from rest_framework.views import APIView

from brapi.models.observation import (ObsVariable, Datatype, Ontology,
                                      ObsVariableSerializer, DatatypeSerializer,
                                      OntologySerializer)

from brapi.aux_fun import paginate, search_post_params_in

from brapi.apps import BrAPIListPagination


class DatatypesViewSet(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = DatatypeSerializer
    pagination_class = BrAPIListPagination
    queryset = Datatype.objects.all()

# end class DatatypesViewSet


class OntologiesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Ontology.objects.all()
    serializer_class = OntologySerializer

# end class OntologiesViewSet
    
    
class ObsVariablesView(APIView):
    
    serializer_class = ObsVariableSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = ObsVariable.objects.all()

        observationVariableDbId = self.kwargs.get('observationVariableDbId', None)
        if observationVariableDbId is not None:
            queryset = queryset.filter(observationVariableDbId=observationVariableDbId)
        # end if

        return paginate(queryset, request, 'ObsVariableSerializer')

    # end def get_queryset

# end class ObsVariablesView


class ObsVariablesListView(APIView):
    
    serializer_class = ObsVariableSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = ObsVariable.objects.all()

        # this search is not standard since it is on a related table
        param_value = self.request.query_params.get('traitClass', None)
        if param_value is not None:
            queryset = queryset.filter(trait__classe=param_value)
        # end if

        return paginate(queryset, request, 'ObsVariableSerializer')

    # end def get

# end class ObsVariablesListView


class VSearchView(APIView):

    serializer_class = ObsVariableSerializer

    def post(self, request, format=None, *args, **kwargs):
        
        queryset = ObsVariable.objects.all()

        # TODO: add ('datatypes'), ('traitClasses')
        queryset = search_post_params_in(self, queryset, [('observationVariableDbId', 'observationVariableDbIds'),
            ('ontologyXref', 'ontologyXrefs'),
            ('ontologyDbId', 'ontologyDbIds'),
            ('method', 'methodDbIds'),
            ('scale', 'scaleDbIds'),
            ('name', 'names')])

        return paginate(queryset, request, 'ObsVariableSerializer')

    # end def post

# end class VSearchView
