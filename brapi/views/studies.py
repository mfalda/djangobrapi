from rest_framework import viewsets
from rest_framework.views import APIView

from brapi.models import (StudyType, StudySeason, StudyObservationLevel,
                                Study)
from brapi.serializers import (StudySerializer,
                                StudyTypeSerializer, StudySeasonSerializer, 
                                StudyObservationLevelSerializer)

#from brapi.models.germplasm import Germplasm, GermplasmSerializer
#from brapi.models.observation import ObsVariable, ObsVariableSerializer

from brapi.aux_fun import search_get_qparams, search_post_params_in, paginate

from brapi.paginators import BrAPIListPagination


#class StudyObsUnitsView(APIView):
#
#    serializer_class = StudyObsUnitSerializer
#
#
#    def get(self, request, format=None, *args, **kwargs):
#        
#        queryset = StudyObsUnit.objects.all()
#
#        queryset = search_post_params_in(self, queryset, [('observationVariableDbIds', 'observationVariableDbIds')])
#    
#        return paginate(queryset, request, StudyObsVariableSerializer)
#
#    # end def get
#    
## end class StudyObsUnitsView
    

# class SSearchView(APIView):
#
#     serializer_class = StudyObsUnitSerializer
#
#
#     def get(self, request, format=None, *args, **kwargs):
#
#         queryset = Study.objects.all()
#
#         queryset = search_get_qparams(self, queryset, [('studyType', 'studyType'),
#             ('seasonDbId', 'seasonDbId'),
#             ('locationDbId', 'locationDbId'),
#             ('programDbId', 'programDbId'),
#             ('germplasmDbId', 'germplasmDbIds'),
#             ('observationVariableDbId', 'observationVariableDbIds'),
#             ('active', 'active')])
#
#         return paginate(queryset, request, StudySerializer)
#
#     # end def get
#
#
#     def post(self, request, format=None, *args, **kwargs):
#
#         queryset = Study.objects.all()
#
#         queryset = search_post_params_in(self, queryset, [('studyType', 'studyType'),
#             ('seasonDbId', 'seasonDbId'),
#             ('locationDbId', 'locationDbId'),
#             ('programDbId', 'programDbId'),
#             ('germplasmDbId', 'germplasmDbIds'),
#             ('observationVariableDbId', 'observationVariableDbIds'),
#             ('active', 'active')])
#
#         return paginate(queryset, request, StudySerializer)
#
#     # end def post
#
# # end class SSearchView
#
#
# class StudyObsUnitsView(APIView):
#
#     serializer_class = StudyObsUnitSerializer
#
#     def get(self, request, format=None, *args, **kwargs):
#
#         queryset = StudyObsUnit.objects.all()
#         queryset = search_get_qparams(self, queryset,
#                    [('observationVariableDbIds', 'observationVariableDbIds')])
#
#         return paginate(queryset, request, StudyObsUnitSerializer)
#
#     # end def get
#
# # end class StudyObsUnitsView
#
#
# class StudyObsUnitsDetailsView(APIView):
#
#     serializer_class = StudyObsUnitSerializer
#
#
#     def get(self, request, format=None, *args, **kwargs):
#
#         queryset = StudyObsUnit.objects.all()
#
#         return paginate(queryset, request, StudyObsUnitSerializer)
#
#     # end def get
#
# # end class StudyObsUnitsDetailsView


class StudySeasonsViewSet(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = StudySeasonSerializer

    def get_queryset(self):

        queryset = StudySeason.objects.all()

        return search_get_qparams(self, queryset, [('year', 'year')])

    # end def get_queryset

# end class StudySeasonsViewSet


class StudyTypesViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = StudyType.objects.all()
    serializer_class = StudyTypeSerializer

# end class StudyTypesViewSet


class StudyObservationLevelViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = StudyObservationLevel.objects.all()
    pagination_class = BrAPIListPagination    
    serializer_class = StudyObservationLevelSerializer

# end class StudyObservationLevelViewSet


class StudyDetailsView(APIView):
    
    serializer_class = StudySerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = Study.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            queryset = queryset.filter(studyDbId=studyDbId)
        # end if
        
        return paginate(queryset, request, StudySerializer)

    # end def get
    
# end class StudyDetailsView

#
# class StudyGermplasmDetailsView(APIView):
#
#     serializer_class = GermplasmSerializer
#
#
#     def get(self, request, format=None, *args, **kwargs):
#
#         queryset = Germplasm.objects.all()
#
#         studyDbId = self.kwargs.get('studyDbId', None)
#         if studyDbId is not None:
#             queryset = queryset.filter(study__studyDbId=studyDbId)
#         # end if
#
#         return paginate(queryset, request, GermplasmSerializer)
#
#     # end def get
#
# # end class StudyGermplasmDetailsView
#
#
# class StudyObsUnitsTableView(APIView):
#
#     serializer_class = StudyObsUnitSerializer
#
#
#     def get(self, request, format=None, *args, **kwargs):
#
#         queryset = StudyObsUnit.objects.all()
#
#         return paginate(queryset, request, StudyObsUnitSerializer)
#
#     # end def get
#
# # end class StudyObsUnitsTableView
#
#
# class StudyObsVarsView(APIView):
#
#     serializer_class = ObsVariableSerializer
#
#
#     def get(self, request, format=None, *args, **kwargs):
#
#         queryset = StudyObsUnit.objects.all()
#
#         studyDbId = self.kwargs.get('studyDbId', None)
#         if studyDbId is not None:
#             queryset = queryset.filter(studyDbId=studyDbId)
#         # end if
#
#         return paginate(queryset, request, StudyObsUnitSerializer)
#
#     # end def get
#
# # end class StudyObsVarsView
#
#
# # cannot use ViewSets nor generic views because the detail view is not standard
# class StudyPlotView(APIView):
#
#     queryset = StudyPlot.objects.all()
#     serializer_class = StudyPlotSerializer
#
#     def get(self, request, format=None, *args, **kwargs):
#
#         queryset = StudyPlot.objects.all()
#
#         studyDbId = self.kwargs.get('studyDbId', None)
#         if studyDbId is not None:
#             queryset = queryset.filter(studyDbId=studyDbId)
#         # end if
#
#         return paginate(queryset, request, StudyPlotSerializer)
#
#     # end def get
#
# # end class StudyPlotView
