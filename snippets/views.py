from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route


# the DefaultRouter class we're using in urls.py  also automatically creates the API root view

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # deal with pre-rendered HTML
    # the @detail_route decorator creates a custom action named highlight (that don't fit into the standard create/update/delete actions)
    # custom actions which use the @detail_route decorator will respond to GET requests by default
    # we can use the methods argument if we wanted an action that responded to POST requests
    # if you want to change the way URLs should be constructed, you can include url_path as a decorator keyword argument
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # to associate the user that created the snippet with the snippet instance
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
