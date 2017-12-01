from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class CallsTest(APITestCase):

    fixtures = ['crops.json', 'calls.json']
    

    def test_get_calls(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 25,
            "totalCount": 50,
            "pageSize": 2
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
                    "call": "germplasm//markerprofiles",
                    "datatypes": [
                        "json"
                    ],
                    "methods": [
                        "GET"
                    ]
            }
        ]
    }
}"""
                
        test_get(self, '/brapi/v1/calls?pageSize=2', expected)

    # end def test_get_calls

# end class CallTest
