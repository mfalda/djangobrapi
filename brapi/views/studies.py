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

from brapi.aux_fun import search_get_qparams, search_post_params_in, paginate
from brapi.paginators import BrAPIListPagination, BrAPISimplePagination

class StudySearchView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Study.objects.all()

        queryset = search_get_qparams(self, queryset, [
            ('studyType', 'studyType'),
            ('seasonDbId', 'seasons__seasonDbId'),
            ('locationDbId', 'locationDbId'),
            ('programDbId', 'trialDbId__programDbId'),
            ('germplasmDbIds', 'studies__germplasmDbId'),
            ('observationVariableDbIds', 'studies__observations__obsVariable__observationVariableDbId')])

        # 'active' parameter must be managed in a non-standard way
        active = self.request.query_params.get('active', None)
        if active is not None:
            if active == 'true':
                queryset = queryset.filter(active=True)
            elif active == 'false':
                queryset = queryset.filter(active=False)
                # end if
        # end if

        logger = logging.getLogger(__name__)

        sortBy = self.request.query_params.get('sortBy', None)
        sortOrder = self.request.query_params.get('sortOrder', None)
        logger.warning("Sorting: (%s, %s)" % (sortBy, sortOrder))

        if sortBy is not None:
            if sortOrder is not None and sortOrder == 'asc':
                logger.warning("Sorting by %s in ascending mode" % sortBy)
                queryset = queryset.order_by(sortBy)
            elif sortOrder is not None and sortOrder == 'desc':
                logger.warning("Sorting by %s in descending mode" % sortBy)
                queryset = queryset.order_by('-' + sortBy)
            # end if
        # end if

        #queryset = queryset.distinct()

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

        # TODO: studyType should be an exact search
        queryset = search_post_params_in(self, queryset, [
            ('studyType', 'studyType'),
            ('studyNames', 'studyName'),
            ('studyLocations', 'locationDbId__name'),
            ('programNames', 'trialDbId__programDbId__name'),
            ('germplasmDbIds', 'studies__germplasmDbId'),
            ('trialDbIds', 'trialDbId__trialDbId'),
            ('observationVariableDbIds', 'studies__observations__obsVariable__observationVariableDbId')])

        # 'active' parameter must be managed in a non-standard way
        active = self.request.data.get('active', None)
        if active is not None:
            if active == 'true':
                queryset = queryset.filter(active=True)
            elif active == 'true':
                queryset = queryset.filter(active=False)
                # end if
        # end if

        logger = logging.getLogger(__name__)

        sortBy = self.request.data.get('sortBy', None)
        sortOrder = self.request.data.get('sortOrder', None)
        logger.warning("Sorting: (%s, %s)" % (sortBy, sortOrder))

        if sortBy is not None:
            if sortOrder is not None and sortOrder == 'asc':
                logger.warning("Sorting by %s in ascending mode" % sortBy)
                queryset = queryset.order_by(sortBy)
            elif sortOrder is not None and sortOrder == 'desc':
                logger.warning("Sorting by %s in descending mode" % sortBy)
                queryset = queryset.order_by('-' + sortBy)
                # end if
        # end if

        # WHY is it necessary?
        queryset = queryset.distinct()

        return paginate(queryset, request, StudySearchSerializer)

    # end def post

# end class StudySearchView


class StudyObservationUnitByObservationVariableView(APIView):

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


class StudySeasonView(APIView):
    
    def get(self, request, format=None, *args, **kwargs):

        queryset = Season.objects.all()

        queryset = search_get_qparams(self, queryset, [('year', 'year')])

        return paginate(queryset, request, SeasonSerializer)

    # end def get

# end class StudySeasonView


class StudyTypeView(APIView):
    
    def get(self, request, format=None, *args, **kwargs):

        queryset = StudyType.objects.all()

        return paginate(queryset, request, StudyTypeSerializer)

    # end def get

# end class StudyTypeView


class StudyObservationLevelView(APIView):
    
    def get(self, request, format=None, *args, **kwargs):

        queryset = StudyObservationLevel.objects.all()

        return paginate(queryset, request, StudyObservationLevelSerializer, BrAPIListPagination)

     # end def get

# end class StudyObservationLevelView


class StudyDetailView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        
        queryset = Study.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        logger = logging.getLogger(__name__)
        logger.warning("Got study ID %s" % studyDbId)

        if studyDbId is not None:
            queryset = queryset.filter(studyDbId=studyDbId)
        # end if
        
        return paginate(queryset, request, StudySerializer, BrAPISimplePagination)

    # end def get
    
# end class StudyDetailView


class StudyGermplasmDetailsView(APIView):

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

    def get(self, request, format=None, *args, **kwargs):

        queryset = ObservationUnit.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            queryset = queryset.filter(studyDbId=studyDbId)
        # end if

        return paginate(queryset, request, StudyPlotLayoutSerializer)

    # end def get

# end class StudyPlotLayoutView
