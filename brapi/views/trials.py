from rest_framework.views import APIView

# there is a circular dependency between trials and studies (when aggregationg models and serializers)
from brapi.models.study import Trial, TrialSerializer

from brapi.aux_fun import search_get_qparams, paginate


class TrialView(APIView):

    serializer_class = TrialSerializer


    def get(self, request, format=None, *args, **kwargs):
    
        queryset = Trial.objects.all()
        queryset = search_get_qparams(self, queryset, [('programDbId', 'programDbId'), ('locationDbId', 'locationDbId'),
                                    ('active', 'active')])
            
        sortBy = self.request.query_params.get('sortBy', None)
        sortOrder = self.request.query_params.get('sortOrder', None)

        if sortBy is not None:
            if sortOrder is not None and sortOrder == 'Ascending':
                queryset = queryset.order_by(sortBy)
            elif sortOrder is not None and sortOrder == 'Descending':
                queryset = queryset.order_by('-' + sortBy)
            # end if
        # end if

        return paginate(queryset, request, TrialSerializer)

    # end def get

# end class TrialView
    

class TrialDetailsView(APIView):

    serializer_class = TrialSerializer

    def get(self, request, format=None, *args, **kwargs):
    
        queryset = Trial.objects.all()
        
        trialDbId = self.kwargs.get('trialDbId', None)
        if trialDbId is not None:
            queryset = queryset.filter(trialDbId=trialDbId)
        # end if

        return paginate(queryset, request, TrialSerializer)

    # end def get

# end class TrialDetailsView
