from rest_framework.views import APIView

from brapi.models import Location
from brapi.serializers import LocationSerializer
from brapi.aux_fun import search_get_qparams, paginate
from brapi.paginators import BrAPISimplePagination


class LocationView(APIView):

    def get(self, request, format=None, *args, **kwargs):
    
        queryset = Location.objects.all()
        
        queryset = search_get_qparams(self, queryset, [('locationType', 'type')])

        return paginate(queryset, request, LocationSerializer)

    # end def get

# end class LocationView
    

class LocationDetailsView(APIView):

     def get(self, request, format=None, *args, **kwargs):
    
        queryset = Location.objects.all()
        
        locationDbId = self.kwargs.get('locationDbId', None)
        if locationDbId is not None:
            queryset = queryset.filter(locationDbId=locationDbId)
        # end if

        return paginate(queryset, request, LocationSerializer, BrAPISimplePagination)

    # end def get

# end class LocationDetailsView
