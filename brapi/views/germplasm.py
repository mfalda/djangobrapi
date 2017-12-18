from rest_framework.views import APIView
import logging

from brapi.models import Germplasm, Pedigree
from brapi.serializers import GermplasmSerializer, PedigreeSerializer

from brapi.aux_fun import search_get_qparams, search_post_params_in, paginate


class GermplasmView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Germplasm.objects.all()

        germplasmDbId = self.kwargs.get('germplasmDbId', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if

        return paginate(queryset, request, GermplasmSerializer)

    # end def get

# end class GermplasmView


class GermplasmPedigreeView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Pedigree.objects.all()

        germplasmDbId = self.kwargs.get('germplasmDbId', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if

        notation = self.request.query_params.get('notation', None)

        if notation is not None:
            raise Exception('Deal with "notation" parameter')
        # end if

        return paginate(queryset, request, PedigreeSerializer)

    # end def get

# end class GermplasmPedigreeView


class GermplasmSearchView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Germplasm.objects.all()

        logger = logging.getLogger(__name__)
        logger.warning("Searching with parameters %s" % self.request.query_params)

        queryset = search_get_qparams(self, queryset, [('germplasmName', 'germplasmName'), 
            ('germplasmDbId', 'germplasmDbId'), ('germplasmPUI', 'germplasmPUI')])

        return paginate(queryset, request, GermplasmSerializer)

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
        logger.warning("Parameters: %s" % params)

        queryset = search_post_params_in(self, queryset, [('germplasmNames', 'germplasmName'), 
                ('germplasmDbId', 'germplasmDbId'), ('germplasmPUIs', 'germplasmPUI'), 
                ('germplasmSpecies', 'germplasmSpecies'), ('germplasmGenus', 'germplasmGenus'),
                ('accessionNumbers', 'accessionNumber')])

        return paginate(queryset, request, GermplasmSerializer)         

    # end def post

# end class GermplasmSearchView
