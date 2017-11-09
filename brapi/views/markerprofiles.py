from rest_framework import viewsets
from rest_framework.views import APIView
import logging

from brapi.models.markerprofile import (AlleleMatrix, AlleleMSearch, 
                                        MarkerProfile, GPMarkerP,
                                        AlleleMatrixSerializer, AlleleMSearchSerializer,
                                        MarkerProfileSerializer, GPMarkerPSerializer)
from brapi.aux_fun import search_get_qparams, search_post_params_in, paginate

from brapi.paginators import BrAPIListPagination


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
    
    serializer_class = MarkerProfileSerializer


    def get(self, request, format=None, *args, **kwargs):
    
        queryset = MarkerProfile.objects.all()

        markerprofileDbId = self.kwargs.get('markerprofileDbId', None)
        
        logger = logging.getLogger(__name__)
        logger.warn("Markerprofiles data: %s" % markerprofileDbId)

        if markerprofileDbId is not None:
            queryset = queryset.filter(markerProfilesDbId=markerprofileDbId)
        # end if

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=

        return paginate(queryset, request, MarkerProfileSerializer)

    # end def get

# end class MarkerProfilesDataView


class MarkerProfilesView(APIView):

    serializer_class = MarkerProfileSerializer


    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)
        logger.warn("Searching with parameters %s" % self.request.query_params)

        queryset = MarkerProfile.objects.all()

        queryset = search_get_qparams(self, queryset, [('germplasmDbId', 'germplasm'),
            ('studyDbId', 'studyDbId'), ('sampleDbId', 'sample'), ('extractDbId', 'extract'),
            ('analysisMethod', 'method')])

        return paginate(queryset, request, MarkerProfileSerializer)

    # end def get


    def post(self, request, format=None, *args, **kwargs):
        
        params = self.request.data

        logger = logging.getLogger(__name__)
        logger.warn("Searching with parameters: %s" % params)
        
        queryset = MarkerProfile.objects.all()

        queryset = search_post_params_in(self, queryset, [('germplasmDbId', 'germplasm'),
            ('studyDbId', 'studyDbId'), ('sampleDbId', 'sample'), ('extractDbId', 'extract'),
            ('analysisMethod', 'method')])
    
        return paginate(queryset, request, MarkerProfileSerializer)

    # end def post

# end class MarkerProfilesView


class GPMarkerPView(APIView):

    serializer_class = GPMarkerPSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = GPMarkerP.objects.all()

        germplasmDbId = self.kwargs.get('id', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if        

        return paginate(queryset, request, GPMarkerPSerializer)

    # end def get

# end class GPMarkerPView