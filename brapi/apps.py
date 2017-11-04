from django.apps import AppConfig
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class BrAPIConfig(AppConfig):
    
    name = 'brapi'
    
# end class BrAPIConfig
    

def _paginate_queryset(self, queryset, request, view=None):

    page_size = self.get_page_size(request)
    if not page_size:
        return None

    paginator = self.django_paginator_class(queryset, page_size)
    page_number = request.query_params.get(self.page_query_param, 1)
    if page_number in self.last_page_strings:
        page_number = paginator.num_pages

    try:
        self.page = paginator.page(page_number)
    except InvalidPage as exc:
        msg = self.invalid_page_message.format(
            page_number=page_number, message=six.text_type(exc)
        )
        raise NotFound(msg)

    if paginator.num_pages > 1 and self.template is not None:
        # The browsable API should display pagination controls.
        self.display_page_controls = True

    self.request = request

    return list(self.page)
  
# end def paginate_queryset

    
class BrAPIResultsSetPagination(PageNumberPagination):
    
    page_size_query_param = 'pageSize'
    request = None


    def paginate_queryset(self, queryset, request, view=None):
    
        self.request = request
        return _paginate_queryset(self, queryset, request, view)

    # end def paginate_queryset
    
    
    def get_paginated_response(self, data):

        return Response({
            'metadata': {
                'pagination': {
                    'currentPage': self.page.number,
                    'pageTotal': self.page.paginator.num_pages,
                    'totalCount': self.page.paginator.count,
                    'pageSize': self.get_page_size(self.request)
                },
                'status': [],
                'datafiles': []
            },
            'result': {
                'data': data
            }
        })

    # end def get_paginated_response

# end class BrAPIResultsSetPagination


class BrAPIListPagination(PageNumberPagination):
    
    page_size_query_param = 'pageSize'
    request = None


    def paginate_queryset(self, queryset, request, view=None):
    
        self.request = request
        return _paginate_queryset(self, queryset, request, view)
        
    # end def paginate_queryset
    
    
    def get_paginated_response(self, data):

        return Response({
            'metadata': {
                'pagination': {
                    'currentPage': self.page.number,
                    'pageTotal': self.page.paginator.num_pages,
                    'totalCount': self.page.paginator.count,
                    'pageSize': self.get_page_size(self.request)
                },
                'status': [],
                'datafiles': []
            },
            'result': {
                'data': [list(d.values())[0] for d in data]
            }
        })

    # end def get_paginated_response

# end class BrAPIListPagination
    