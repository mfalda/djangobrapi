from rest_framework import viewsets

from brapi.models.location import Location, LocationSerializer

from brapi.aux_fun import search_get_qparams


# cannot use ViewSets because the previous detail view is not standard
class LocationViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = LocationSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned records
        """

        queryset = Location.objects.all()

        return search_get_qparams(self, queryset, [('locationType', 'locationType')])

    # end def get_queryset

# end class LocationViewSet
