from rest_framework.views import APIView
import logging

from brapi.models import Sample
from brapi.serializers import SampleSerializer
from brapi.aux_fun import paginate


class SampleView(APIView):

    def get(self, request, format=None, *args, **kwargs):

        queryset = Sample.objects.all()

        sampleId = self.kwargs.get('sampleId', None)
        logger = logging.getLogger(__name__)
        logger.warning("Sample id '%s'" % sampleId)
        
        if sampleId is not None:
            queryset = queryset.filter(sampleId=sampleId)
        # end if        

        return paginate(queryset, request, SampleSerializer)

    # end def get

# end class SampleView
