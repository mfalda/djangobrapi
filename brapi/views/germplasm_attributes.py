from rest_framework import viewsets
from rest_framework.views import APIView
import logging

from brapi.models import GermplasmAttributeCategory, GermplasmAttribute, GermplasmAttributeValue
from brapi.serializers import (GermplasmAttributeCategorySerializer, GermplasmAttributeSerializer,
                               GermplasmAttributeValueSerializer)

from brapi.aux_fun import paginate


class GermplasmAttributesListViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = GermplasmAttributeCategorySerializer
    queryset = GermplasmAttributeCategory.objects.all()

# end class GermplasmAttributesListViewSet


class GermplasmAttributesAvailailableViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = GermplasmAttributeSerializer
    queryset = GermplasmAttribute.objects.all()

# end class GermplasmAttributesAvailailableViewSet


class GermplasmAttributeView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = GermplasmAttributeValue.objects.all()

        germplasmDbId = self.kwargs.get('germplasmDbId', None)
        if germplasmDbId is not None:
            queryset = queryset.filter(germplasmDbId=germplasmDbId)
        # end if

        attributeDbIds = self.request.query_params.get('attributeList', None)

        logger = logging.getLogger(__name__)
        logger.warning("FILTERING: %s (IN %s)" % (germplasmDbId, attributeDbIds))

        if attributeDbIds is not None:
            queryset = queryset.filter(attributeDbId__in=attributeDbIds)
        # end if

        return paginate(queryset, request, GermplasmAttributeValueSerializer)
         
    # end def get

# end class GermplasmAttributeView
