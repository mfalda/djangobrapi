from django.apps import AppConfig
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.request import Request


class BrAPIConfig(AppConfig):
    name = 'brapi'


class BrAPIResultsSetPagination(pagination.PageNumberPagination):
    
    page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):

        return Response({
            'metadata': {
                'pagination': {
                    'currentPage': self.page.number,
                    'pageTotal': self.page.paginator.num_pages,
                    'totalCount': self.page.paginator.count,
                    'pageSize': self.page_size
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


class BrAPIListPagination(pagination.PageNumberPagination):
    
    page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):

        return Response({
            'metadata': {
                'pagination': {
                    'currentPage': self.page.number,
                    'pageTotal': self.page.paginator.num_pages,
                    'totalCount': self.page.paginator.count,
                    'pageSize': self.page_size
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