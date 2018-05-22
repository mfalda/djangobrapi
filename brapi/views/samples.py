from rest_framework.views import APIView
import logging

from brapi.models import Sample
from brapi.serializers import SampleSerializer
from brapi.aux_fun import paginate, search_get_qparams, search_post_params_in
from brapi.paginators import BrAPISimplePagination


class SampleView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Sample.objects.all()

        sampleId = self.kwargs.get('sampleId', None)
        logger = logging.getLogger(__name__)
        logger.warning("Sample id '%s'" % sampleId)
        
        if sampleId is not None:
            queryset = queryset.filter(sampleDbId=sampleId)
        # end if        

        return paginate(queryset, request, SampleSerializer, BrAPISimplePagination)

    # end def get

# end class SampleView


class SampleSearchView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Sample.objects.all()
        queryset = search_get_qparams(self, queryset,
                                      [('sampleDbId', 'samplebid'),
                                       ('observationUnitDbId', 'observationunitdbid'),
                                       #('plateDbId', 'platedbid'),
                                       #('germplasmDbIdtype', 'germplasmdbidtype')
                                      ])

        return paginate(queryset, request, SampleSerializer)

    # end def get

    def post(self, request, format=None, *args, **kwargs):

        # PARAMS:
        # {
        #     "sampleDbId" : ["Unique-Plant-SampleID-1", "Unique-Plant-SampleID-2"],
        #     "observationUnitDbId" : ["abc123", "a1b2c3"],
        #     "plateDbId" : ["PlateID-123"],
        #     "germplasmDbIdtype": ["def456"],
        #     "sortBy" : "sampleDbId",
        #     "sortOrder" : "desc",
        #     "pageSize": 1000,
        #     "page": 0,
        # }

        queryset = Sample.objects.all()

        # TODO: studyType should be an exact search
        queryset = search_post_params_in(self, queryset, [
            ('sampleDbId', 'samplebid'),
            ('observationUnitDbId', 'observationunitdbid'),
            #('plateDbId', 'platedbid'),
            #('germplasmDbIdtype', 'germplasmdbidtype')
        ])

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

        return paginate(queryset, request, SampleSerializer)

    # end def post

# end class SampleSearchView

