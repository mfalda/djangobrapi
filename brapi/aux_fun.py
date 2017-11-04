from rest_framework.response import Response

from brapi.apps import BrAPIResultsSetPagination


# the DefaultRouter class we're using in urls.py  also automatically creates the API root view


def _search_get_qparams(self, queryset, params):

    #  [('name', 'name'), ('type', 'type'), ('matchMethod', 'matchMethod'), ('include', 'synonyms')]
    for (param_name, search) in params:
        param_value = self.request.query_params.get(param_name, None)
        if param_value is not None:
            queryset = queryset.filter(**{search: param_value})
        # end if
    # end for

    return queryset

# end def _search_get_qparams


def _search_post_params_in(self, queryset, params):
    
    #  [('name', 'name'), ('type', 'type'), ('matchMethod', 'matchMethod'), ('include', 'synonyms')]
    for (search, param_name) in params:
        param_value = self.request.data.get(param_name, None)
        if param_value is not None:
            queryset = queryset.filter(**{search + '__in': param_value})
        # end if
    # end for

    return queryset

# end def _search_post_params_in


def _paginate(queryset, request, serializer, paginator_class=BrAPIResultsSetPagination):
    
    paginator = paginator_class(request)

    page = paginator.paginate_queryset(queryset, request)
    if page is not None:
        serializer = eval('%s(page, many=True)' % serializer)
        return paginator.get_paginated_response(serializer.data, request.data.get('pageSize', 100))
    else:
        serializer = eval('%s(queryset, many=True)' % serializer)
        return Response(serializer.data)        
    # end if

# end def _paginate
