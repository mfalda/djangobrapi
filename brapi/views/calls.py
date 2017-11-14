#from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework.views import APIView
from brapi.models.call import Call, CallsSerializer

from brapi.aux_fun import paginate


class CallsView(APIView):#ProtectedResourceView):

    serializer_class = CallsSerializer

    def get(self, request, format=None, *args, **kwargs):

        queryset = Call.objects.all()

        return paginate(queryset, request, CallsSerializer)

    # end def get

# end class CallsView