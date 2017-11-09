from rest_framework.views import exception_handler
 
 
def brapi_exception_handler(exc, context):
    
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
 
    if response is not None:
        response.data = """    
{ 
  "metadata" : {
       "pagination": {
          "pageSize":0, 
          "currentPage":0, 
          "totalCount":0, 
          "totalPages":0 
      },
      "status" : [ {
          "message": "%s",
          "code" : %s 
      } ],
      "datafiles": []
  },
  "result": {}
  }""" % (response.data['detail'], response.status_code)

    # end if
 
    return response

# end def brapi_exception_handler
