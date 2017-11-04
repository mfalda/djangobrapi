from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.calls import CallsViewSet
from brapi.models.call import Call


class CallsTest(APITestCase):

    def setUp(self):

        Call.objects.create(call='token', datatypes=['json', 'text'], methods=['POST', 'DELETE'])
        Call.objects.create(call='calls', datatypes=['json'], methods=['GET'])

    # end def setUP


    def test_get_calls(self):

        view = CallsViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/v1/calls/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content` without this.
        self.assertJSONEqual(response.content.decode('utf-8'), """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 2,
            "pageSize": 100
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
                {
                    "call": "token",
                    "datatypes": [
                        "json",
                        "text"
                    ],
                    "methods": [
                        "POST",
                        "DELETE"
                    ]
                },
                {
                    "call": "calls",
                    "datatypes": [
                        "json"
                    ],
                    "methods": [
                        "GET"
                    ]
            }
        ]
    }
}""")

    # end def test_get_calls

# end class CallTest
