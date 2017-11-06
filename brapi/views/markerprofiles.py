from rest_framework import viewsets
from rest_framework.views import APIView
import logging

from brapi.models.markerprofile import (AlleleMatrix, AlleleMSearch, 
                                        MarkerProfile, MarkerProfilesData,
                                        AlleleMatrixSerializer, AlleleMSearchSerializer,
                                        MarkerProfileSerializer, MarkerProfilesDataSerializer)

from brapi.aux_fun import search_get_qparams, search_post_params_in, paginate

from brapi.apps import BrAPIListPagination


class AlleleMatrixViewSet(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = AlleleMatrixSerializer

    def get_queryset(self):

        queryset = AlleleMatrix.objects.all()

        return search_get_qparams(self, queryset, [('studyDbId', 'studyDbId')])

    # end def get_queryset

# end class AlleleMatrixViewSet


class AlleleMSearchView(APIView):
    
    serializer_class = AlleleMSearchSerializer


    def get(self, request, format=None, *args, **kwargs):
        
        queryset = AlleleMSearch.objects.all()

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=
        queryset = search_get_qparams(self, queryset, [('markerprofileDbId', 'markerprofileDbId'), ('markerDbId', 'markerDbId')])

        return paginate(queryset, request, AlleleMSearchSerializer, BrAPIListPagination)

    # end def get

       
    def post(self, request, format=None, *args, **kwargs):
            
        queryset = AlleleMSearch.objects.all()

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=
        queryset = search_post_params_in(self, queryset, [('markerprofileDbId', 'markerprofileDbId'), ('markerDbId', 'markerDbId')])

        return paginate(queryset, request, AlleleMSearchSerializer, BrAPIListPagination)

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

        return paginate(queryset, request, MarkerProfilesDataSerializer)

    # end def get

# end class MarkerProfilesDataView


class MarkerProfilesView(APIView):

    serializer_class = MarkerProfileSerializer


    def get(self, request, format=None, *args, **kwargs):
    
        queryset = MarkerProfile.objects.all()

        queryset = search_get_qparams(self, queryset, [('germplasm', 'germplasmDbId'),
            ('studyDbId', 'studyDbId'), ('sample', 'sampleDbId'), ('extract', 'extractDbId'),
            ('method', 'analysisMethod')])

        return paginate(queryset, request, MarkerProfileSerializer)

    # end def get


    def post(self, request, format=None, *args, **kwargs):
        
        queryset = MarkerProfile.objects.all()

        queryset = search_post_params_in(self, queryset, [('germplasm', 'germplasmDbId'),
            ('studyDbId', 'studyDbId'), ('sample', 'sampleDbId'), ('extract', 'extractDbId'),
            ('method', 'analysisMethod')])

        return paginate(queryset, request, MarkerProfileSerializer)

    # end def post

# end class MarkerProfilesView
