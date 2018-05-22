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

        queryset = search_get_qparams(self, queryset, [('studyDbId', 'studyDbId')])

        return paginate(queryset, request, AlleleMatrixSerializer)

    # end def get

# end class AlleleMatrixView


class AlleleMatrixSearchView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = MarkerprofileData.objects.all()

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=
        # TODO: implement the parameter matrixDbId
        queryset = search_get_qparams(self, queryset, [('markerprofileDbId', 'markerprofileDbId'),
                                                       ('markerDbId', 'markerDbId')]) #, ('matrixDbId', 'matrixDbId')])

        return paginate(queryset, request, AlleleMatrixSearchSerializer, BrAPISimplePagination)

    # end def get


    def post(self, request, format=None, *args, **kwargs):

        # PARAMS:
        # {
        #     "markerprofileDbId": ["993","994","995], // (required) The markerprofile db ids. Not Required if 'markerDbId' or 'matrixDbId' is present.
        #     "markerDbId": ["322","323","324"], // (required) ids of the markers. if none are specified, results are returned for all markers in the database. Not Required if 'markerprofileDbId' or 'matrixDbId' is present.
        #     "matrixDbId": ["457","458","459"], // (required) ids of the complete matrix. Not Required if 'markerprofileDbId' or 'markerDbId' is present.
        #     "expandHomozygotes" : true,  //(optional) Should homozygotes NOT be collapsed into a single orrucance?
        #     "unknownString" : "-", //(optional) The string to use as a representation for missing data.
        #     "sepPhased" : "|",  //(optional) The string to use as a separator for phased allele calls.
        #     "sepUnphased" : "/", // (optional)The string to use as a separator for unphased allele calls.
        #     "format" : "tsv", // (optional) If specified, this indicates that the server should return the data in the specified data format. The link to the data file is then returned in the "datafiles" field of the "metadata". Initially only "tsv" is supported which returns the data in a tab-delimited format. MarkerprofileDbIds along the top, markerDbIds along the side and allele calls in the center.
        #     "pageSize" : 100, // (optional)the number of allele calls reported per response page.
        #     "page" : 1 // (optional) the requested response page
        # }

        queryset = MarkerprofileData.objects.all()

        # TODO: it is not clear to which data the query parameters apply!
        # unknownString=&sepPhased=&sepUnphased=&expandHomozygotes=
        # TODO: implement the parameter matrixDbId
        queryset = search_post_params_in(self, queryset, [('markerprofileDbId', 'markerprofileDbId'),
                                                          ('markerDbId', 'markerDbId')]) #, ('matrixDbId', 'matrixDbId')])

        return paginate(queryset, request, AlleleMatrixSearchSerializer, BrAPISimplePagination)

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
                                                       ('studyDbId', 'studyDbId'),
                                                       ('sample', 'sampleDbId'),
                                                       ('extract', 'extractDbId'),
                                                       ('method', 'analysisMethod')])

        return paginate(queryset, request, MarkerprofileSerializer)

    # end def get


    def post(self, request, format=None, *args, **kwargs):

        params = self.request.data

        logger = logging.getLogger(__name__)
        logger.warning("Searching with parameters: %s" % params)

        queryset = Markerprofile.objects.all()

        queryset = search_post_params_in(self, queryset, [('germplasm', 'germplasmDbId'),
                                                          ('studyDbId', 'studyDbId'),
                                                          ('sample', 'sampleDbId'),
                                                          ('extract', 'extractDbId'),
                                                          ('method', 'analysisMethod')], False)

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

        return paginate(queryset, request, GermplasmMarkerprofileSerializer, BrAPISimplePagination)

    # end def get

# end class GermplasmMarkeprofileView
