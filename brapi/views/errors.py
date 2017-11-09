from rest_framework.exceptions import APIException
from brapi.exception_handlers import brapi_exception_handler


def error400(request):
    
    raise brapi_exception_handler("Bad request!")

# end def error400


def error404(request):
    
    raise brapi_exception_handler("Page not found!")

# end def error404