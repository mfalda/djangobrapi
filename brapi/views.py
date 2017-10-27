from brapi.models import Call, Location, Crop
from brapi.serializers import CallsSerializer, LocationSerializer, CropSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from brapi.apps import BrAPIResultsSetPagination, BrAPIListPagination
from rest_framework.views import APIView


# the DefaultRouter class we're using in urls.py  also automatically creates the API root view

class CallsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = Call.objects.all()
    serializer_class = CallsSerializer
    paginate_by_param = 'pageSize'

# end class CallsViewSet


class CropViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    serializer_class = CropSerializer
    paginate_by_param = 'pageSize'
    pagination_class = BrAPIListPagination
    queryset = Crop.objects.all()

# end class CropViewSet


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    serializer_class = LocationSerializer
    paginate_by_param = 'pageSize'

    def get_queryset(self):
        """
        Optionally restricts the returned records
        """

        queryset = Location.objects.all()

        location_type = self.request.query_params.get('locationType', None)
        if location_type is not None:
            queryset = queryset.filter(locationType=location_type)
        # end if
        
        return queryset
    
    # end def get_queryset

# end class LocationViewSet
