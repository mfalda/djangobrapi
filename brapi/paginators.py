from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
import six


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
  
# end def _paginate_queryset

    
class BrAPIResultsSetPagination(PageNumberPagination):
    
    page_size_query_param = 'pageSize'
    request = None


    def paginate_queryset(self, queryset, request, view=None):
    
        self.request = request
        return _paginate_queryset(self, queryset, request, view)

    # end def paginate_queryset
    
    
    def get_paginated_response(self, data, extra=None):

        res = Response({
            "metadata": {
                "pagination": {
                    "currentPage": self.page.number,
                    "totalPages": self.page.paginator.num_pages,
                    "totalCount": self.page.paginator.count,
                    "pageSize": self.get_page_size(self.request)
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "data": data
            }
        })
        if extra is not None:
            #print('RESULT:' + str(res.__dict__))
            res.data['result'].update(extra)
        # end if

        return res

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
            "metadata": {
                "pagination": {
                    "currentPage": self.page.number,
                    "totalPages": self.page.paginator.num_pages,
                    "totalCount": self.page.paginator.count,
                    "pageSize": self.get_page_size(self.request)
                },
                "status": [],
                "datafiles": []
            },
            "result": {
                "data": [list(d.values())[0] for d in data]
            }
        })

    # end def get_paginated_response

# end class BrAPIListPagination


class BrAPISimplePagination(PageNumberPagination):

    page_size_query_param = 'pageSize'
    request = None


    def paginate_queryset(self, queryset, request, view=None):

        self.request = request
        return _paginate_queryset(self, queryset, request, view)

    # end def paginate_queryset


    def get_paginated_response(self, data):

        return Response({
            "metadata": {
                "pagination": {
                    "currentPage": self.page.number,
                    "totalPages": self.page.paginator.num_pages,
                    "totalCount": self.page.paginator.count,
                    "pageSize": self.get_page_size(self.request)
                },
                "status": [],
                "datafiles": []
            },
            "result": data[0]
        })

    # end def get_paginated_response

# end class BrAPISimplePagination
