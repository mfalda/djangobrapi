from rest_framework import serializers
from django.contrib.auth.models import User
from brapi.models import Call


 # using hyperlinks and URLs instead of RDBMs IDs and foreign keys
class CallsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Call
        fields = ('url', 'id', 'call', 'datatypes', 'methods')

    # end class Meta

# end class CallsSerializer

