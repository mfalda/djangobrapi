from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class ProgramTest(APITestCase):
    
    fixtures = ['programs.json']


    def test_get_programs(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 3,
            "totalCount": 6,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "programDbId": 1,
                "name": "CIPHQ",
                "abbreviation": "CIPHQ",
                "objective": "Global Population Improvement",
                "leadPerson": "G. Leader"
            },
            {
                "programDbId": 2,
                "name": "Ghana",
                "abbreviation": "GHA",
                "objective": "OFSP",
                "leadPerson": "M. Breeder"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/programs/?pageSize=2', expected)
        
    # end def test_get_programs


    def test_post_search(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 1,
            "pageSize": 100
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "programDbId": 1,
                "name": "CIPHQ",
                "abbreviation": "CIPHQ",
                "objective": "Global Population Improvement",
                "leadPerson": "G. Leader"
            }
        ]
    }
}"""
        params = {
            "programDbId": 1
        }
        
        test_post(self, '/brapi/v1/programs-search', params, expected)

    # end def test_post_search

# end class ProgramTest
