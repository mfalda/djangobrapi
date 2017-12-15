from rest_framework import viewsets
from rest_framework.views import APIView
import logging
from pprint import pformat

from brapi.models import (StudyType, Season, StudyObservationLevel, Observation,
                                Study, ObservationUnit, ObservationVariable, Germplasm)

from brapi.serializers import (StudySerializer, StudySearchSerializer,
                                StudyTypeSerializer, SeasonSerializer,
                                StudyObservationLevelSerializer, StudyPlotLayoutSerializer,
                                ObservationVariableSerializer, StudyGermplasmSerializer,
                                ObservationUnitSerializer, StudyObservationUnitByObservationVariableSerializer)

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


class StudyObservationUnitByObservationVariableView(APIView):

    serializer_class = StudyObservationUnitByObservationVariableSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = None

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            # get the ObservationUnits
            queryset = Observation.objects.filter(observationUnit__studyDbId=studyDbId)

            queryset = search_get_qparams(self, queryset,
                   [('observationVariableDbIds', 'obsVariable')])
        # end if

        return paginate(queryset, request, StudyObservationUnitByObservationVariableSerializer)

    # end def get

# end class StudyObservationUnitByObservationVariableView


class StudyObservationUnitDetailsView(APIView):

    serializer_class = ObservationUnitSerializer


    def get(self, request, format=None, *args, **kwargs):

        queryset = ObservationUnit.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        logger = logging.getLogger(__name__)
        logger.warning("Got study ID %s" % studyDbId)

        if studyDbId is not None:
            queryset = queryset.filter(studyDbId=studyDbId)
        # end if

        observationLevel = self.request.query_params.get('observationLevel', None)

        if observationLevel is not None:
            queryset = queryset.filter(observationLevel=observationLevel)
        # end if

        return paginate(queryset, request, ObservationUnitSerializer)

    # end def get

# end class StudyObservationUnitDetailsView


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


class StudyGermplasmDetailsView(APIView):

    serializer_class = StudyGermplasmSerializer


    def get(self, request, format=None, *args, **kwargs):

        queryset = None

        logger = logging.getLogger(__name__)

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            # get the ObservationUnit
            ou = ObservationUnit.objects.filter(studyDbId=studyDbId)
            logger.warning("ObservationUnits: %s" % str([pformat(ou.__dict__) for ou in ou]))

            # get the Germplasm
            g = Germplasm.objects.all()
            # and filter them
            queryset = g.filter(germplasmDbId__in=ou)
            logger.warning("Obs. variables: %s" % str([pformat(g.__dict__) for g in g]))
        # end if

        return paginate(queryset, request, StudyGermplasmSerializer)

    # end def get

# end class StudyGermplasmDetailsView


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


class StudyObservationVariableView(APIView):

    serializer_class = ObservationVariableSerializer


    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            # get the Observation
            obs = Observation.objects.filter(observationUnit__studyDbId=studyDbId)
            logger.warning("Observations: %s" % str([pformat(o.__dict__) for o in obs]))

            # get the ObservationVariables
            ov = ObservationVariable.objects.all()
            # and filter them
            queryset = ov.filter(observationVariableDbId__in=ov)
            logger.warning("Obs. variables: %s" % str([pformat(queryset.__dict__) for ov in ov]))
        # end if

        return paginate(queryset, request, ObservationVariableSerializer)

    # end def get

# end class StudyObservationVariableView


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
