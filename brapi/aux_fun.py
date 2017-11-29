from rest_framework.response import Response
import json
#from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status

from brapi.paginators import BrAPIResultsSetPagination


# the DefaultRouter class we're using in urls.py  also automatically creates the API root view


def search_get_qparams(self, queryset, params):

    #  [('name', 'name'), ('type', 'type'), ('matchMethod', 'matchMethod'), ('include', 'synonyms')]
    for (param_name, search) in params:
        param_value = self.request.query_params.get(param_name, None)
        if param_value is not None:
            queryset = queryset.filter(**{search: param_value})
        # end if
    # end for

    return queryset

# end def search_get_qparams


def search_post_params_in(self, queryset, params, in_=True):
    
    #  [('name', 'name'), ('type', 'type'), ('matchMethod', 'matchMethod'), ('include', 'synonyms')]
    for (search, param_name) in params:
        param_value = self.request.data.get(param_name, None)
        if param_value is not None:
            if in_:
                search += '__in'
            # end if
            queryset = queryset.filter(**{search: param_value})
        # end if
    # end for

    return queryset

# end def search_post_params_in


def paginate(queryset, request, Serializer, paginator_class=BrAPIResultsSetPagination):
    
    paginator = paginator_class()

    page = paginator.paginate_queryset(queryset, request)
    if page is not None:
        serializer = Serializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        serializer = Serializer(queryset, many=True)
        return Response(serializer.data)        
    # end if

# end def paginate


def test_get(self, url, expected):
    
    #token = Token.objects.get(user__username='marco')
    client = APIClient(enforce_csrf_checks=True)
    #client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    self.maxDiff = None
    
    response.render() # Cannot access `response.content` without this.
    self.assertJSONEqual(response.content.decode('utf-8'), expected)
                             
# end def test_get
    
    
def test_post(self, url, params, expected):
    
    #token = Token.objects.get(user__username='marco')
    client = APIClient(enforce_csrf_checks=True)
    #client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = client.post(url, json.dumps(params), content_type='application/json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    self.maxDiff = None

    response.render() # Cannot access `response.content` without this.
    self.assertJSONEqual(response.content.decode('utf-8'), expected)

# end def test_post
    