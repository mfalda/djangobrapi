from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # REST framework's reverse function returns fully-qualified URLs
        # URL patterns are identified by convenience names declared in snippets/urls.py
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # to associate the user that created the snippet with the snippet instance
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # ensure that authenticated requests get read-write access, and unauthenticated requests get read-only access
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


# use the base class for representing instances, and create our own .get()
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    # deali with pre-rendered HTML
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


# read-only view
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# read-only view
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
