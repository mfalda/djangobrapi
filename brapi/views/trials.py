from rest_framework.views import APIView
import logging

from brapi.models import Trial
from brapi.serializers import TrialSerializer
from brapi.aux_fun import search_get_qparams, paginate


class TrialView(APIView):

    def get(self, request, format=None, *args, **kwargs):
    
        queryset = Trial.objects.all()
        queryset = search_get_qparams(self, queryset, [
            ('programDbId', 'programDbId'),
            ('locationDbId', 'studies__locationDbId')])

        # 'active' parameter must be managed in a non-standard way
        active = self.request.query_params.get('active', None)
        if active is not None:
            if active == 'true':
                queryset = queryset.filter(active=True)
            elif active == 'false':
                queryset = queryset.filter(active=False)
            # end if
        # end if

        logger = logging.getLogger(__name__)

        sortBy = self.request.query_params.get('sortBy', None)
        sortOrder = self.request.query_params.get('sortOrder', None)
        logger.warning("Sorting: (%s, %s)" % (sortBy, sortOrder))

        if sortBy is not None:
            if sortOrder is not None and sortOrder == 'asc':
                logger.warning("Sorting by %s in ascending mode" % sortBy)
                queryset = queryset.order_by(sortBy)
            elif sortOrder is not None and sortOrder == 'desc':
                logger.warning("Sorting by %s in descending mode" % sortBy)
                queryset = queryset.order_by('-' + sortBy)
            # end if
        # end if

        return paginate(queryset, request, TrialSerializer)

    # end def get

# end class TrialView
    

class TrialDetailsView(APIView):

    def get(self, request, format=None, *args, **kwargs):
    
        queryset = Trial.objects.all()
        
        trialDbId = self.kwargs.get('trialDbId', None)
        if trialDbId is not None:
            queryset = queryset.filter(trialDbId=trialDbId)
        # end if

        return paginate(queryset, request, TrialSerializer)

    # end def get

# end class TrialDetailsView
