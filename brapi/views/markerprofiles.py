from rest_framework.views import APIView
import logging

from brapi.models import (AlleleMatrix, Markerprofile, MarkerprofileData)

from brapi.serializers import (AlleleMatrixSerializer, AlleleMatrixSearchSerializer,
                                MarkerprofileSerializer, GermplasmMarkerprofileSerializer,
                               MarkerprofileDataSerializer)

from brapi.aux_fun import search_get_qparams, search_post_params_in, paginate
from brapi.paginators import BrAPIListPagination, BrAPISimplePagination


class AlleleMatrixView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = AlleleMatrix.objects.all()

        return paginate(queryset, request, AlleleMatrixSerializer)

    # end def get

# end class AlleleMatrixView


class AlleleMatrixSearchView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = MarkerprofileData.objects.all()

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=
        queryset = search_get_qparams(self, queryset, [('markerprofileDbId', 'markerprofileDbId'), ('markerDbId', 'markerDbId')])

        return paginate(queryset, request, AlleleMatrixSearchSerializer, BrAPIListPagination)

    # end def get


    def post(self, request, format=None, *args, **kwargs):

        queryset = MarkerprofileData.objects.all()

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=
        queryset = search_post_params_in(self, queryset, [('markerprofileDbId', 'markerprofileDbId'), ('markerDbId', 'markerDbId')])

        return paginate(queryset, request, AlleleMatrixSearchSerializer, BrAPIListPagination)

    # end def post


# end class AlleleMatrixSearchView


class MarkerprofileDataView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Markerprofile.objects.all()

        markerprofileDbId = self.kwargs.get('markerprofileDbId', None)
        if markerprofileDbId is not None:
            queryset = queryset.filter(markerprofileDbId=markerprofileDbId)
        # end if

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=

        return paginate(queryset, request, MarkerprofileDataSerializer, BrAPISimplePagination)

    # end def get

# end class MarkerprofileDataView


class MarkerprofileView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)
        logger.warning("Searching with parameters %s" % self.request.query_params)

        queryset = Markerprofile.objects.all()

        queryset = search_get_qparams(self, queryset, [('germplasm', 'germplasmDbId'),
            ('studyDbId', 'studyDbId'), ('sample', 'sampleDbId'), ('extract', 'extractDbId'),
            ('method', 'analysisMethod')])

        return paginate(queryset, request, MarkerprofileSerializer)

    # end def get


    def post(self, request, format=None, *args, **kwargs):

        params = self.request.data

        logger = logging.getLogger(__name__)
        logger.warning("Searching with parameters: %s" % params)

        queryset = Markerprofile.objects.all()

        queryset = search_post_params_in(self, queryset, [('germplasmDbId', 'germplasm'),
            ('studyDbId', 'studyDbId'), ('sampleDbId', 'sample'), ('extractDbId', 'extract'),
            ('analysisMethod', 'method')])

        return paginate(queryset, request, MarkerprofileSerializer)

    # end def post

# end class MarkerprofileView


class GermplasmMarkeprofileView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Markerprofile.objects.all()

        germplasmDbId = self.kwargs.get('id', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)[:1]
        # end if

        return paginate(queryset, request, GermplasmMarkerprofileSerializer)

    # end def get

# end class GermplasmMarkeprofileView