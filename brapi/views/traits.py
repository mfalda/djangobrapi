from rest_framework import viewsets

from brapi.models.trait import Trait, TraitSerializer


class TraitViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TraitSerializer
    queryset = Trait.objects.all()

# end class TraitViewSet
