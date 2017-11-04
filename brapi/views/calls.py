from rest_framework import viewsets

from brapi.models.call import Call, CallsSerializer


class CallsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = Call.objects.all()
    serializer_class = CallsSerializer

# end class CallsViewSet
