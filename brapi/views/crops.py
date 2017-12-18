from rest_framework.views import APIView

from brapi.models import Crop
from brapi.serializers import CropSerializer
from brapi.paginators import BrAPIListPagination
from brapi.aux_fun import paginate


class CropsView(APIView):#ProtectedResourceView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Crop.objects.all()

        return paginate(queryset, request, CropSerializer, BrAPIListPagination)

    # end def get

# end class CropsView