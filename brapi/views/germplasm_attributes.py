from rest_framework import viewsets
from rest_framework.views import APIView
import logging

from brapi.models.germplasm_attributes import (GAList, GermplasmAttr, GAAttrAvail, 
                                               GAListSerializer, GermplasmAttrSerializer,
                                               GAAttrAvailSerializer)

from brapi.aux_fun import paginate


class GAListViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = GAListSerializer
    queryset = GAList.objects.all()

# end class GAListViewSet


class GAAttrAvailViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = GAAttrAvailSerializer
    queryset = GAAttrAvail.objects.all()

# end class GAAttrAvailViewSet


class GermplasmAttrView(APIView):

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

        return paginate(queryset, request, GermplasmAttrSerializer)
         
    # end def get

# end class GermplasmAttrView
