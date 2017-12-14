from rest_framework import viewsets
from rest_framework.views import APIView
import logging

from brapi.models import (StudyType, Season, StudyObservationLevel,
                                Study, ObservationUnit)
from brapi.serializers import (StudySerializer, StudySearchSerializer,
                                StudyTypeSerializer, SeasonSerializer,
                                StudyObservationLevelSerializer, StudyPlotLayoutSerializer)

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
    

class StudySearchView(APIView):

    serializer_class = StudySerializer


    def get(self, request, format=None, *args, **kwargs):

        queryset = Study.objects.all()

        queryset = search_get_qparams(self, queryset, [
            ('studyType', 'studyType'),
            ('seasonDbId', 'seasonDbId'),
            ('locationDbId', 'locationDbId'),
            ('programDbId', 'programDbId'),
            ('germplasmDbId', 'germplasmDbIds'),
            ('observationVariableDbId', 'observationVariableDbIds'),
            ('active', 'active')])

        return paginate(queryset, request, StudySearchSerializer)

    # end def get


    def post(self, request, format=None, *args, **kwargs):

        # PARAMS:
        # {
        #     "studyType" : "Trial",
        #     "studyNames" : ["Study A", "StydyB"],
        #     "studyLocations" : ["Kenya", "Zimbabwe"],
        #     "programNames": ["Test Program", "Program2"],
        #     "germplasmDbIds" : [ "CML123", "CWL123"],
        #     "trialDbIds" : [ "7", "8"],
        #     "observationVariableDbIds": ["CO-PH-123", "Var-123"]
        #     "active" : "true",
        #     "sortBy" : "studyDbId",
        #     "sortOrder" : "desc",
        #     "pageSize": 1000,
        #     "page": 0,
        # }

        queryset = Study.objects.all()

        queryset = search_post_params_in(self, queryset, [
            ('studyType', 'studyType'),
            ('seasonDbId', 'seasonDbId'),
            ('locationDbId', 'locationDbId'),
            ('programDbId', 'programDbId'),
            ('germplasmDbId', 'germplasmDbIds'),
            ('observationVariableDbId', 'observationVariableDbIds'),
            ('active', 'active')])

        return paginate(queryset, request, StudySearchSerializer)

    # end def post

# end class StudySearchView


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


class StudySeasonViewSet(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = SeasonSerializer

    def get_queryset(self):

        queryset = Season.objects.all()

        return search_get_qparams(self, queryset, [('year', 'year')])

    # end def get_queryset

# end class StudySeasonViewSet


class StudyTypeViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = StudyType.objects.all()
    serializer_class = StudyTypeSerializer

# end class StudyTypeViewSet


class StudyObservationLevelViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = StudyObservationLevel.objects.all()
    pagination_class = BrAPIListPagination    
    serializer_class = StudyObservationLevelSerializer

# end class StudyObservationLevelViewSet


class StudyDetailView(APIView):
    
    serializer_class = StudySerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = Study.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        logger = logging.getLogger(__name__)
        logger.warning("Got study ID %s" % studyDbId)

        if studyDbId is not None:
            queryset = queryset.filter(studyDbId=studyDbId)
        # end if
        
        return paginate(queryset, request, StudySerializer)

    # end def get
    
# end class StudyDetailView

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
# cannot use ViewSets nor generic views because the detail view is not standard
class StudyPlotLayoutView(APIView):

    queryset = ObservationUnit.objects.all()
    serializer_class = StudyPlotLayoutSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = ObservationUnit.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            queryset = queryset.filter(studyDbId=studyDbId)
        # end if

        return paginate(queryset, request, StudyPlotLayoutSerializer)

    # end def get

# end class StudyPlotLayoutView
