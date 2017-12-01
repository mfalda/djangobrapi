from rest_framework import viewsets


from brapi.models import Crop
from brapi.serializers import CropSerializer
from brapi.paginators import BrAPIListPagination


class CropsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CropSerializer
    pagination_class = BrAPIListPagination
    queryset = Crop.objects.all()

# end class CropsViewSet
