#from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework.views import APIView
from brapi.models import Call
from brapi.serializers import CallSerializer

from brapi.aux_fun import paginate


class CallsView(APIView):#ProtectedResourceView):

    serializer_class = CallSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = Call.objects.all()

        return paginate(queryset, request, CallSerializer)

    # end def get

# end class CallsView
