from django.shortcuts import render


def index(request):

    return render(request, 'brapi/index.html', {})

# end def index
