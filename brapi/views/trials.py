from rest_framework import viewsets

# there is a circular dependency between trials and studies (when aggregationg models and serializers)
from brapi.models.study import Trial, TrialSerializer

from brapi.aux_fun import _search_get_qparams


class TrialViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TrialSerializer

    def get_queryset(self):
    
        queryset = Trial.objects.all()
        queryset = _search_get_qparams(self, queryset, [('programDbId', 'programDbId'), ('locationDbId', 'locationDbId'),
                                    ('active', 'active')])
            
        sortBy = self.request.query_params.get('sortBy', None)
        sortOrder = self.request.query_params.get('sortOrder', None)

        if sortBy is not None:
            if sortOrder is not None and sortOrder == 'Ascending':
                queryset = queryset.order_by(sortBy)
            elif sortOrder is not None and sortOrder == 'Descending':
                queryset = queryset.order_by('-' + sortBy)
            # end if

        return queryset

    # end def get_queryset

# end class TrialViewSet
