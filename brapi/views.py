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
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from requests.exceptions import HTTPError
from social_django.utils import psa

from brapi.models import (Call, Trait, Crop, Program, Location, Map, MapLinkage, Marker, Trait, 
    GAList, GAAttrAvail, GermplasmAttr, Germplasm, GPPedigree, GPDonor, GPMarkerP, Trial,
    Sample, Phenotype, Datatype, Ontology, StudySeason, StudyType, StudyObsLevel,
    StudyPlot, AlleleMatrix, AlleleMSearch, MarkerProfile, MarkerProfilesData,
    ObsVValue, ObsScale, ObsMethod, ObsTrait, ObsVariable, StudyObsUnit, Study)

from brapi.serializers import (SocialSerializer, CallsSerializer, LocationSerializer, CropSerializer,
    ProgramSerializer, MapSerializer, MapLinkageSerializer, MarkerSerializer, TraitSerializer,
    GAListSerializer, GAAttrAvailSerializer, GermplasmAttrSerializer, GermplasmSerializer, 
    GPPedigreeSerializer, GPDonorSerializer, GPMarkerPSerializer, TrialSerializer, SampleSerializer,
    PhenotypeSerializer, DatatypeSerializer, OntologySerializer, StudySeasonSerializer, StudyTypeSerializer,
    StudyObsLevelSerializer, StudyPlotSerializer, AlleleMatrixSerializer, AlleleMSearchSerializer,
    MarkerProfileSerializer, MarkerProfilesDataSerializer, ObsVValueSerializer, ObsScaleSerializer,
    ObsTraitSerializer, ObsMethodSerializer, ObsVariableSerializer, StudyObsUnitSerializer, StudySerializer)


# the DefaultRouter class we're using in urls.py  also automatically creates the API root view


@api_view(http_method_names=['POST'])
@permission_classes([AllowAny])
@psa()
def exchange_token(request, backend):
    """
    Exchange an OAuth2 access token for one for this site.
    This simply defers the entire OAuth2 process to the front end.
    The front end becomes responsible for handling the entirety of the
    OAuth2 process; we just step in at the end and use the access token
    to populate some user identity.
    The URL at which this view lives must include a backend field, like:
        url(API_ROOT + r'social/(?P<backend>[^/]+)/$', exchange_token),
    Using that example, you could call this endpoint using i.e.
        POST API_ROOT + 'social/facebook/'
        POST API_ROOT + 'social/google-oauth2/'
    Note that those endpoint examples are verbatim according to the
    PSA backends which we configured in settings.py. If you wish to enable
    other social authentication backends, they'll get their own endpoints
    automatically according to PSA.
    ## Request format
    Requests must include the following field
    - `access_token`: The OAuth2 access token provided by the provider
    """
    serializer = SocialSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # set up non-field errors key
        # http://www.django-rest-framework.org/api-guide/exceptions/#exception-handling-in-rest-framework-views
        try:
            nfe = settings.NON_FIELD_ERRORS_KEY
        except AttributeError:
            nfe = 'non_field_errors'
        # end try

        try:
            # this line, plus the psa decorator above, are all that's necessary to
            # get and populate a user object for any properly enabled/configured backend
            # which python-social-auth can handle.
            user = request.backend.do_auth(serializer.validated_data['access_token'])
        except HTTPError as e:
            # An HTTPError bubbled up from the request to the social auth provider.
            # This happens, at least in Google's case, every time you send a malformed
            # or incorrect access key.
            return Response(
                {'errors': {
                    'token': 'Invalid token',
                    'detail': str(e),
                }},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # end try

        if user:
            if user.is_active:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                # user is not active; at some point they deleted their account,
                # or were banned by a superuser. They can't just log in with their
                # normal credentials anymore, so they can't log in with social
                # credentials either.
                return Response(
                    {'errors': {nfe: 'This user account is inactive'}},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # end if
        else:
            # Unfortunately, PSA swallows any information the backend provider
            # generated as to why specifically the authentication failed;
            # this makes it tough to debug except by examining the server logs.
            return Response(
                {'errors': {nfe: "Authentication Failed"}},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # end if
    # end if

# end def exchange_token
 

def _search_get_qparams(self, queryset, params):

    #  [('name', 'name'), ('type', 'type'), ('matchMethod', 'matchMethod'), ('include', 'synonyms')]
    for (param_name, search) in params:
        param_value = self.request.query_params.get(param_name, None)
        if param_value is not None:
            queryset = queryset.filter(**{search: param_value})
        # end if
    # end for

    return queryset

# end def _search_get_qparams


def _search_post_params_in(self, queryset, params):
    
    #  [('name', 'name'), ('type', 'type'), ('matchMethod', 'matchMethod'), ('include', 'synonyms')]
    for (search, param_name) in params:
        param_value = self.request.data.get(param_name, None)
        if param_value is not None:
            queryset = queryset.filter(**{search + '__in': param_value})
        # end if
    # end for

    return queryset

# end def _search_post_params_in


def _paginate(queryset, request, serializer, paginator_class=BrAPIResultsSetPagination):
    
    paginator = paginator_class()

    page = paginator.paginate_queryset(queryset, request)
    if page is not None:
        serializer = eval('%s(page, many=True)' % serializer)
        return paginator.get_paginated_response(serializer.data)
    else:
        serializer = SampleSerializer(queryset, many=True)
        return Response(serializer.data)        
    # end if

# end def _paginate


class CallsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = Call.objects.all()
    serializer_class = CallsSerializer

# end class CallsViewSet


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProgramSerializer

    def get_queryset(self):

        queryset = Program.objects.all()

        return _search_get_qparams(self, queryset, [('programName', 'programName'), ('abbreviation', 'abbreviation')])

    # end def get_queryset

# end class ProgramViewSet


class CropsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CropSerializer
    pagination_class = BrAPIListPagination
    queryset = Crop.objects.all()

# end class CropsViewSet


class MapViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):

        self.serializer_class = MapSerializer
        queryset = Map.objects.all()

        return _search_get_qparams(self, queryset, [('type', 'type'), ('species', 'species')])

    # end def get_queryset

# end class MapViewSet


class MapLinkageView(generics.ListCreateAPIView):

    serializer_class = MapLinkageSerializer

    def get_queryset(self):

        logger = logging.getLogger(__name__)

        mapDbId = self.kwargs['mapDbId']
        queryset = MapLinkage.objects.all()

        linkageGroupId = self.request.query_params.get('linkageGroupId', None)
        logger.warn("Linkages: (%s, %s)" % (mapDbId, linkageGroupId))

        return _search_get_qparams(self, queryset, [('mapDbId', 'mapDbId'), ('linkageGroupId', 'linkageGroupId')])

    # end def get_queryset

# end class MapLinkageView


# cannot use ViewSets nor generic views because the detail view is not standard
class MapLinkageViewPositions(APIView):

    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)

        mapDbId = self.kwargs['mapDbId']
        queryset = MapLinkage.objects.all()

        linkageGroupId = self.kwargs['linkageGroupId']
        logger.warn("Positions: (%s, %s)" % (mapDbId, linkageGroupId))

        queryset = queryset.filter(Q(mapDbId=mapDbId)&Q(linkageGroupId=linkageGroupId))

        # numerical filters, therefore cannot use '_search_get_qparams'
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

    def get_queryset(self):
        """
        Optionally restricts the returned records
        """

        queryset = Location.objects.all()

        return _search_get_qparams(self, queryset, [('locationType', 'locationType')])

    # end def get_queryset

# end class LocationViewSet


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

        return _search_get_qparams(self, queryset, [('type', 'type')])

    # end def get_queryset

# end class MarkerViewSet


class TraitViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TraitSerializer
    queryset = Trait.objects.all()

# end class TraitViewSet


class GAListViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = GAListSerializer
    queryset = GAList.objects.all()

# end class GAListViewSet


class GAAttrAvailViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = GAAttrAvailSerializer
    queryset = GAAttrAvail.objects.all()

# end class GAAttrAvailViewSet


class GermplasmAttrView(APIView):

    serializer_class = GermplasmSerializer    

    def get(self, request, format=None, *args, **kwargs):

        queryset = GermplasmAttr.objects.all()

        germplasmDbId = self.kwargs.get('germplasmDbId', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if

        attributeDbIds = self.request.query_params.get('attributeList', None)

        logger = logging.getLogger(__name__)
        logger.warn("FILTERING: %s (IN %s)" % (germplasmDbId, attributeDbIds))

        if attributeDbIds is not None:
            queryset = queryset.filter(attributeDbId__in=attributeDbIds)
        # end if

        serializer = GermplasmAttrSerializer(queryset, many=True)

        return Response(serializer.data)           

    # end def get

# end class GermplasmAttrView


class GermplasmView(APIView):

    serializer_class = GermplasmSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = Germplasm.objects.all()

        germplasmDbId = self.kwargs.get('germplasmDbId', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if        

        serializer = GermplasmSerializer(queryset, many=True)

        return Response(serializer.data)           

    # end def get

# end class GermplasmView


class GPPedigreeView(APIView):

    serializer_class = GPPedigreeSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = GPPedigree.objects.all()

        germplasmDbId = self.kwargs.get('germplasmDbId', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if        

        notation = self.request.query_params.get('notation', None)

        if notation is not None:
            raise Exception('Deal with "notation" parameter')
        # end if

        return _paginate(queryset, request, 'GPPedigreeSerializer')

    # end def get

# end class GPPedigreeView


class GPMarkerPView(APIView):

    serializer_class = GPMarkerPSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = GPMarkerP.objects.all()

        germplasmDbId = self.kwargs.get('id', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if        

        return _paginate(queryset, request, 'GPMarkerPSerializer')

    # end def get

# end class GPMarkerPView


class GermplasmSearchView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)

        queryset = Germplasm.objects.all()

        logger = logging.getLogger(__name__)
        logger.warn("Searching with parameters %s" % self.request.query_params)

        queryset = _search_get_qparams(self, queryset, [('germplasmName', 'germplasmName'), 
            ('germplasmDdId', 'germplasmDdId'), ('germplasmPUI', 'germplasmPUI')])

        serializer = GermplasmSerializer(queryset, many=True)

        return Response(serializer.data)           

    # end def get


    def post(self, request, format=None, *args, **kwargs):

        queryset = Germplasm.objects.all()

        # PARAMS:
        # {
        #     "germplasmPUIs" : [ "http://www.crop-diversity.org/mgis/accession/01BEL084609", "doi:10.15454/328757862534E12" ],
        #     "germplasmDbIds" : [ "986", "01BEL084609" ],
        #     "germplasmSpecies" : [ "aestivum", "vinifera" ],
        #     "germplasmGenus" : [ "Solanum", "Triticum" ],
        #     "germplasmNames" : [ "XYZ1", "Pahang" ],
        #     "accessionNumbers": [ "ITC0609", "ITC0685" ],
        #     "pageSize" : 100,
        #     "page": 1
        # }

        params = self.request.data

        logger = logging.getLogger(__name__)
        logger.warn("Parameters: %s" % params)

        queryset = _search_post_params_in(self, queryset, [('germplasmNames', 'germplasmNames'), 
                ('germplasmDdIds', 'germplasmDdIds'), ('germplasmPUIs', 'germplasmPUIs'), 
                ('germplasmSpecies', 'germplasmSpecies'), ('germplasmGenus', 'germplasmGenus'),
                ('accessionNumbers', 'accessionNumbers')])

        serializer = GermplasmSerializer(queryset, many=True)

        return Response(serializer.data)           

    # end def post

# end class GermplasmSearchView


class TrialViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TrialSerializer

    def get_queryset(self):
    
        queryset = Trial.objects.all()
        queryset = _search_get_qparams(self, queryset, [('programDbId', 'programDbId'), ('locationDbId', 'locationDbId'),
                                    ('active', 'active')])
            
        sortBy = self.request.query_params.get('sortBy', None)
        sortOrder = self.request.query_params.get('sortOrder', None)

        if sortBy is not None:
            if sortOrder is not None and sortOrder == 'Ascending':
                queryset = queryset.order_by(sortBy)
            elif sortOrder is not None and sortOrder == 'Descending':
                queryset = queryset.order_by('-' + sortBy)
            # end if

        return queryset

    # end def get_queryset

# end class TrialViewSet


class SampleView(APIView):

    serializer_class = SampleSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = Sample.objects.all()

        sampleId = self.kwargs.get('sampleId', None)
        logger = logging.getLogger(__name__)
        logger.warn("Sample id '%s'" % sampleId)
        
        if sampleId is not None:
            queryset = queryset.filter(sampleId=sampleId)
        # end if        

        return _paginate(queryset, request, 'SampleSerializer')

    # end def get

# end class SampleView


class PhenotypeSearchView(APIView):

    def post(self, request, format=None, *args, **kwargs):

        queryset = Phenotype.objects.all()

        # PARAMS:
        # {
        #     "germplasmDbIds" : [ "Blabla", "34Mtp362" ], // (optional, text, `986`) ... The name or synonym of external genebank accession identifiers
        #     "observationVariableDbIds" : [ "37373", "CO_321:00000234"], // (optional, text, `CO_321:00000234`) ... The IDs of traits, could be ontology ID, database ID or PUI
        #     "studyDbIds" : [ "383", "2929", "WHEAT_NETWK_2016_MONTPELLIER" ], // (optional, text, `2356`) ... The database ID / PK of the studies search parameter
        #     "locationDbIds" : [ "383838", "MONTPELLIER" ], // locations these traits were collected
        #     "programDbIds" : [ "3838", "Drought resistance CG 2020" ], // list of programs that have phenotyped this trait
        #     "seasonDbIds" : [ "338", "2010", "1956-2014", "2002-2003-2004", "2007 Spring" ], // (optional, text, `2001`) ... The year or Phenotyping campaign of a multiannual study (trees, grape, ...)
        #     "observationLevel" : "plot", // (optional, text, `plot`) ... The type of the observationUnit. Returns only the observaton unit of the specified type; the parent levels ID can be accessed through observationUnitStructure.
        #     "observationTimeStampRange" : ["2015-06-16T00:53:26-0800","2015-06-18T00:53:26-0800"]
        #     "pageSize" : 100, // (optional, integer, `1000`) ... The size of the pages to be returned. Default is `1000`.
        #     "page" : 1, // (optional, integer, `10`) ... Which result page is requested
        # }

        params = self.request.data

        logger = logging.getLogger(__name__)
        logger.warn("Search parameters: %s" % params)

        queryset = _search_post_params_in(self, queryset, [('germplasmDbIds', 'germplasmDbIds'), 
            ('observationVariableDbIds', 'observationVariableDbIds'), ('studyDbIds', 'studyDbIds'), 
            ('locationDbIds', 'locationDbIds'), ('programDbIds', 'programDbIds'),
            ('seasonDbIds', 'seasonDbIds'), ('observationLevel', 'observationLevel')])

        observationTimeStampRange = params.get('observationTimeStampRange', None)
        if observationTimeStampRange is not None:
            queryset = queryset.filter(Q(observationTimeStampRange__gte=observationTimeStampRange[0])
                                        &Q(observationTimeStampRange__lte=observationTimeStampRange[1]))
        # end if 
        
        serializer = PhenotypeSerializer(queryset, many=True)

        return Response(serializer.data)           

    # end def post

# end class PhenotypeSearchView


class DatatypesViewSet(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = DatatypeSerializer
    pagination_class = BrAPIListPagination
    queryset = Datatype.objects.all()

# end class DatatypesViewSet


class OntologiesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Ontology.objects.all()
    serializer_class = OntologySerializer

# end class OntologiesViewSet


class StudySeasonsViewSet(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = StudySeasonSerializer

    def get_queryset(self):

        queryset = StudySeason.objects.all()

        return _search_get_qparams(self, queryset, [('year', 'year')])

    # end def get_queryset

# end class StudySeasonsViewSet


class StudyTypesViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = StudyType.objects.all()
    serializer_class = StudyTypeSerializer

# end class StudyTypesViewSet


class StudyObsLevelsViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = StudyObsLevel.objects.all()
    pagination_class = BrAPIListPagination    
    serializer_class = StudyObsLevelSerializer

# end class StudyObsLevelsViewSet


# cannot use ViewSets nor generic views because the detail view is not standard
class StudyPlotView(APIView):
    
    queryset = StudyPlot.objects.all()
    serializer_class = StudyPlotSerializer

    def get(self, request, format=None, *args, **kwargs):
    
        queryset = StudyPlot.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            queryset = queryset.filter(studyDbId=studyDbId)
        # end if

        return _paginate(queryset, request, 'StudyPlotSerializer')

    # end def get

# end class StudyPlotView


class AlleleMatrixViewSet(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = AlleleMatrixSerializer

    def get_queryset(self):

        queryset = AlleleMatrix.objects.all()

        return _search_get_qparams(self, queryset, [('studyDbId', 'studyDbId')])

    # end def get_queryset

# end class AlleleMatrixViewSet


class AlleleMSearchView(APIView):
    
    serializer_class = AlleleMSearchSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = AlleleMSearch.objects.all()

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=
        queryset = _search_get_qparams(self, queryset, [('markerprofileDbId', 'markerprofileDbId'), ('markerDbId', 'markerDbId')])

        return _paginate(queryset, request, 'AlleleMSearchSerializer', BrAPIListPagination)

    # end def get

       
    def post(self, request, format=None, *args, **kwargs):
            
        queryset = AlleleMSearch.objects.all()

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=
        queryset = _search_post_params_in(self, queryset, [('markerprofileDbId', 'markerprofileDbId'), ('markerDbId', 'markerDbId')])

        return _paginate(queryset, request, 'AlleleMSearchSerializer', BrAPIListPagination)

    # end def post

         
# end class AlleleMSearchView


class MarkerProfilesDataView(APIView):
    
    serializer_class = MarkerProfilesDataSerializer


    def get(self, request, format=None, *args, **kwargs):
    
        logger = logging.getLogger(__name__)
        logger.warn("Markerprofiles data")

        queryset = MarkerProfilesData.objects.all()

        markerprofileDbId = self.kwargs.get('markerprofileDbId', None)
        if markerprofileDbId is not None:
            queryset = queryset.filter(markerprofileDbId=markerprofileDbId)
        # end if

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=
        queryset = queryset #_search_get_qparams(self, queryset, [('year', 'year')])

        return _paginate(queryset, request, 'MarkerProfilesDataSerializer')

    # end def get

# end class MarkerProfilesDataView


class MarkerProfilesView(APIView):

    serializer_class = MarkerProfileSerializer


    def get(self, request, format=None, *args, **kwargs):
    
        queryset = MarkerProfile.objects.all()

        queryset = _search_get_qparams(self, queryset, [('germplasm', 'germplasmDbId'),
            ('studyDbId', 'studyDbId'), ('sample', 'sampleDbId'), ('extract', 'extractDbId'),
            ('method', 'analysisMethod')])

        return _paginate(queryset, request, 'MarkerProfileSerializer')

    # end def get


    def post(self, request, format=None, *args, **kwargs):
        
        queryset = MarkerProfile.objects.all()

        queryset = _search_post_params_in(self, queryset, [('germplasm', 'germplasmDbId'),
            ('studyDbId', 'studyDbId'), ('sample', 'sampleDbId'), ('extract', 'extractDbId'),
            ('method', 'analysisMethod')])

        return _paginate(queryset, request, 'MarkerProfileSerializer')

    # end def post

# end class MarkerProfilesView


class ObsVariablesView(APIView):
    
    serializer_class = ObsVariableSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = ObsVariable.objects.all()

        observationVariableDbId = self.kwargs.get('observationVariableDbId', None)
        if observationVariableDbId is not None:
            queryset = queryset.filter(observationVariableDbId=observationVariableDbId)
        # end if

        return _paginate(queryset, request, 'ObsVariableSerializer')

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

        return _paginate(queryset, request, 'ObsVariableSerializer')

    # end def get

# end class ObsVariablesListView


class VSearchView(APIView):

    serializer_class = ObsVariableSerializer

    def post(self, request, format=None, *args, **kwargs):
        
        queryset = ObsVariable.objects.all()

        # TODO: add ('datatypes'), ('traitClasses')
        queryset = _search_post_params_in(self, queryset, [('observationVariableDbId', 'observationVariableDbIds'),
            ('ontologyXref', 'ontologyXrefs'),
            ('ontologyDbId', 'ontologyDbIds'),
            ('method', 'methodDbIds'),
            ('scale', 'scaleDbIds'),
            ('name', 'names')])

        return _paginate(queryset, request, 'ObsVariableSerializer')

    # end def post

# end class VSearchView
    
    
class StudyObsUnitsView(APIView):

    serializer_class = StudyObsUnitSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = StudyObsUnit.objects.all()

        queryset = _search_post_params_in(self, queryset, [('observationVariableDbIds', 'observationVariableDbIds')])
    
        return _paginate(queryset, request, 'StudyObsVariableSerializer')

    # end def get
    
# end class StudyObsUnitsView
    

class SSearchView(APIView):

    serializer_class = StudyObsUnitSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = Study.objects.all()

        queryset = _search_get_qparams(self, queryset, [('studyType', 'studyType'),
            ('seasonDbId', 'seasonDbId'),
            ('locationDbId', 'locationDbId'),
            ('programDbId', 'programDbId'),
            ('germplasmDbId', 'germplasmDbIds'),
            ('observationVariableDbId', 'observationVariableDbIds'),
            ('active', 'active')])
    
        return _paginate(queryset, request, 'StudySerializer')

    # end def get


    def post(self, request, format=None, *args, **kwargs):
        
        queryset = Study.objects.all()

        queryset = _search_post_params_in(self, queryset, [('studyType', 'studyType'),
            ('seasonDbId', 'seasonDbId'),
            ('locationDbId', 'locationDbId'),
            ('programDbId', 'programDbId'),
            ('germplasmDbId', 'germplasmDbIds'),
            ('observationVariableDbId', 'observationVariableDbIds'),
            ('active', 'active')])
    
        return _paginate(queryset, request, 'StudySerializer')

    # end def post
    
# end class SSearchView
    

class StudyObsUnitsDetailsView(APIView):

    serializer_class = StudyObsUnitSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = StudyObsUnit.objects.all()

        return _paginate(queryset, request, 'StudyObsUnitSerializer')

    # end def get
    
# end class StudyObsUnitsDetailsView


class StudyDetailsView(APIView):
    
    serializer_class = StudySerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = Study.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            queryset = queryset.filter(studyDbId=studyDbId)
        # end if
        
        return _paginate(queryset, request, 'StudySerializer')

    # end def get
    
# end class StudyDetailsView


class StudyGermplasmDetailsView(APIView):

    serializer_class = GermplasmSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = Germplasm.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            queryset = queryset.filter(study__studyDbId=studyDbId)
        # end if
        
        return _paginate(queryset, request, 'GermplasmSerializer')

    # end def get
    
# end class StudyGermplasmDetailsView


class StudyObsUnitsTableView(APIView):
    
    serializer_class = StudyObsUnitSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = StudyObsUnit.objects.all()

        return _paginate(queryset, request, 'StudyObsUnitSerializer')

    # end def get
    
# end class StudyObsUnitsTableView


class StudyObsVarsView(APIView):
    
    serializer_class = ObsVariableSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = ObsVariable.objects.all()

        studyDbId = self.kwargs.get('studyDbId', None)
        if studyDbId is not None:
            queryset = (queryset.select_related('observations')
                .select_related('observations_units')
                .select_related('studies')
                .filter(studyDbId=studyDbId))
        # end if
        
        return _paginate(queryset, request, 'ObsVariableSerializer')

    # end def get
    
# end class StudyObsVarsView
    