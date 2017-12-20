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


    def test_get_programs_name(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 1,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "objective": "Disease resistance",
                "abbreviation": "DRP1",
                "name": "Wheat Resistance Program",
                "leadPerson": "Dr. Henry Beachell",
                "programDbId": "1"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/programs/?programName=Wheat Resistance Program&pageSize=2', expected)

    # end def test_get_programs_name


    def test_get_programs_abbreviation(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 1,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "leadPerson": "Dr. Norman Borlaug",
                "abbreviation": "DRP2",
                "name": "Wheat Improvement Program",
                "objective": "Yield improvement",
                "programDbId": "2"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/programs/?abbreviation=DRP2&pageSize=2', expected)

    # end def test_get_programs_abbreviation


    def test_post_programs_search(self):

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
                "abbreviation": "DRP1",
                "objective": "Disease resistance",
                "name": "Wheat Resistance Program",
                "leadPerson": "Dr. Henry Beachell",
                "programDbId": "1"
            },
            {
                "abbreviation": "DRP2",
                "objective": "Yield improvement",
                "name": "Wheat Improvement Program",
                "leadPerson": "Dr. Norman Borlaug",
                "programDbId": "2"
            }
        ]
    }
}"""
        params = {}
        
        test_post(self, '/brapi/v1/programs-search?pageSize=2', params, expected)

    # end def test_post_programs_search

# end class ProgramTest
