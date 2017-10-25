from brapi.models import Call
from brapi.serializers import CallsSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route


# the DefaultRouter class we're using in urls.py  also automatically creates the API root view

class CallsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = Call.objects.all()
    serializer_class = CallsSerializer

# end class CallsViewSet