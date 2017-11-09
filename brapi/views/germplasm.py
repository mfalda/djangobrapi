from rest_framework.views import APIView
import logging

from brapi.models.germplasm import (Germplasm, GPPedigree,
                                    GermplasmSerializer, GPPedigreeSerializer)
from brapi.aux_fun import search_get_qparams, search_post_params_in, paginate


class GermplasmView(APIView):

    serializer_class = GermplasmSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = Germplasm.objects.all()

        germplasmDbId = self.kwargs.get('germplasmDbId', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if

        return paginate(queryset, request, GermplasmSerializer)

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

        return paginate(queryset, request, GPPedigreeSerializer)

    # end def get

# end class GPPedigreeView


class GermplasmSearchView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        logger = logging.getLogger(__name__)

        queryset = Germplasm.objects.all()

        logger = logging.getLogger(__name__)
        logger.warn("Searching with parameters %s" % self.request.query_params)

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
        logger.warn("Parameters: %s" % params)

        queryset = search_post_params_in(self, queryset, [('germplasmNames', 'germplasmName'), 
                ('germplasmDbId', 'germplasmDbId'), ('germplasmPUIs', 'germplasmPUI'), 
                ('germplasmSpecies', 'germplasmSpecies'), ('germplasmGenus', 'germplasmGenus'),
                ('accessionNumbers', 'accessionNumber')])

        return paginate(queryset, request, GermplasmSerializer)         

    # end def post

# end class GermplasmSearchView
