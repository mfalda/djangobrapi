from rest_framework import viewsets


from brapi.models.crop import Crop, CropSerializer
from brapi.paginators import BrAPIListPagination


class CropsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CropSerializer
    pagination_class = BrAPIListPagination
    queryset = Crop.objects.all()

# end class CropsViewSet
