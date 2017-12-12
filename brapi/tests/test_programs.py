from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class ProgramTest(APITestCase):
    
    fixtures = ['crops.json', 'programs.json']


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
                "name": "Wheat Resistance Program",
                "abbreviation": "DRP1",
                "leadPerson": "Dr. Henry Beachell",
                "objective": "Disease resistance",
                "programDbId": "1"
            },
            {
                "name": "Wheat Improvement Program",
                "abbreviation": "DRP2",
                "leadPerson": "Dr. Norman Borlaug",
                "objective": "Yield improvement",
                "programDbId": "2"
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
                "programDbId": "1",
                "name": "Wheat Resistance Program",
                "abbreviation": "DRP1",
                "objective": "Disease resistance",
                "leadPerson": "Dr. Henry Beachell"
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
