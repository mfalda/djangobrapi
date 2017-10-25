from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


 # using hyperlinks and URLs instead of RDBMs IDs and foreign keys
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # the untyped ReadOnlyField will be used for serialized representations,
    # but will not be used for updating model instances when they are deserialized.
    # We could have also used CharField(read_only=True) here
    owner = serializers.ReadOnlyField(source='owner.username')
    # only applied to the HTML format
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # one-to-many relation
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
