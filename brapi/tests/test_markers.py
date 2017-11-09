from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class MarkerTest(APITestCase):
    
    fixtures = ['markers.json']


    def test_get_markers(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 3,
            "totalCount": 5,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
{
                "markerDbId": 1,
                "defaultDisplayName": "a_01_10001",
                "type": "SNP",
                "synonyms": [
                    "i_01_10001",
                    "popA_10001"
                ],
                "refAlt": [
                    "A",
                    "T"
                ],
                "analysisMethods": [
                    "illumina"
                ]
            },
            {
                "markerDbId": 2,
                "defaultDisplayName": "A_01_10002",
                "type": "SNP",
                "synonyms": [
                    "i_01_10001",
                    "popA_10002"
                ],
                "refAlt": [
                    "G",
                    "C"
                ],
                "analysisMethods": [
                    "illumina"
                ]
            }
        ]
    }
}"""
            
        test_get(self, '/brapi/v1/markers/?pageSize=2', expected)            

    # end def test_get_markers


    def test_get_marker_details(self):

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
                "markerDbId": 1,
                "defaultDisplayName": "a_01_10001",
                "type": "SNP",
                "synonyms": [
                    "i_01_10001",
                    "popA_10001"
                ],
                "refAlt": [
                    "A",
                    "T"
                ],
                "analysisMethods": [
                    "illumina"
                ]
            }
        ]
    }
}"""
            
        test_get(self, '/brapi/v1/markers/1/', expected)            

    # end def test_get_marker_details
    
# end class MarkerTest
