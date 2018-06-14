from django.shortcuts import render
from brapi.models import Call
from django.db.models import IntegerField
from django.db.models.functions import Cast


def index(request):

    calls = Call.objects.annotate(
        calldbid_int=Cast('calldbid', IntegerField())
    ).order_by('calldbid_int').all()

    return render(request, 'brapi/index.html', {'calls': calls})

# end def index
