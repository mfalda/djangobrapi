from rest_framework.views import APIView

from brapi.models.trait import Trait, TraitSerializer
from brapi.aux_fun import paginate


class TraitView(APIView):

    serializer_class = TraitSerializer


    def get(self, request, format=None, *args, **kwargs):
    
        queryset = Trait.objects.all()

        return paginate(queryset, request, TraitSerializer)

    # end def get

# end class TraitView
    

class TraitDetailsView(APIView):

    serializer_class = TraitSerializer

    def get(self, request, format=None, *args, **kwargs):
    
        queryset = Trait.objects.all()
        
        traitDbId = self.kwargs.get('traitDbId', None)
        if traitDbId is not None:
            queryset = queryset.filter(traitDbId=traitDbId)
        # end if

        return paginate(queryset, request, TraitSerializer)

    # end def get

# end class TraitDetailsView
