from rest_framework.views import APIView
import logging

from brapi.models import GermplasmAttributeCategory, GermplasmAttribute, GermplasmAttributeValue
from brapi.serializers import (GermplasmAttributeCategorySerializer, GermplasmAttributeSerializer,
                               GermplasmAttributeValueSerializer)

from brapi.aux_fun import search_get_qparams, paginate
from brapi.paginators import BrAPISimplePagination


class GermplasmAttributesListView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = GermplasmAttributeCategory.objects.all()

        return paginate(queryset, request, GermplasmAttributeCategorySerializer)

    # end def get

# end class GermplasmAttributesListView


class GermplasmAttributesAvailailableView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = GermplasmAttribute.objects.all()

        queryset = search_get_qparams(self, queryset, [('attributeCategoryDbId', 'attributeCategoryDbId')])

        return paginate(queryset, request, GermplasmAttributeSerializer)

    # end def get

# end class GermplasmAttributesAvailailableView


class GermplasmAttributeView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = GermplasmAttributeValue.objects.all()

        germplasmDbId = self.kwargs.get('germplasmDbId', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if

        attributeDbIds = self.request.query_params.get('attributeList', None)

        logger = logging.getLogger(__name__)
        logger.warning("FILTERING attributes in %s" % attributeDbIds)

        if attributeDbIds is not None:
            queryset = queryset.filter(attributeDbId__in=attributeDbIds.split(','))
        # end if

        return paginate(queryset, request, GermplasmAttributeValueSerializer, BrAPISimplePagination)
         
    # end def get

# end class GermplasmAttributeView
