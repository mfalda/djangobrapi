from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class MarkerProfilesTest(APITestCase):
    
    fixtures = ['allele_matrices.json', 'germplasm.json', 'marker_profiles.json']
    
    
    def test_get_alleleMatrixSearch(self):

        expected = """
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
                "name": "testDs1",
                "matrixDbId": 27,
                "description": "a test dataset",
                "lastUpdated": "2017-06-12",
                "studyDbId": 13
            },
            {
                "name": "testDs2",
                "matrixDbId": 28,
                "description": "a second test dataset",
                "lastUpdated": "2017-06-12",
                "studyDbId": 13
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/allelematrices/', expected)
        
    # end def test_get_alleleMatrixSearch


    def test_get_markerprofiles(self):

        expected = """
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
                "markerProfilesDbId": 3,
                "uniqueDisplayName": "germplasm3",
                "sampleDbId": 33,
                "extractDbId": 1,
                "studyDbId": 1,
                "analysisMethod": "GBS",
                "resultCount": 1,
                "germplasmDbId": 3
            },
            {
                "markerProfilesDbId": 4,
                "uniqueDisplayName": "germplasm4",
                "sampleDbId": 44,
                "extractDbId": 2,
                "studyDbId": 2,
                "analysisMethod": "GoldenGate",
                "resultCount": 1,
                "germplasmDbId": 4
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/markerprofiles', expected)
        
    # end def test_get_markerprofiles


    def test_post_search(self):

        expected = """
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
                "markerProfilesDbId": 3,
                "uniqueDisplayName": "germplasm3",
                "sampleDbId": 33,
                "extractDbId": 1,
                "studyDbId": 1,
                "analysisMethod": "GBS",
                "resultCount": 1,
                "germplasmDbId": 3
            },
            {
                "markerProfilesDbId": 4,
                "uniqueDisplayName": "germplasm4",
                "sampleDbId": 44,
                "extractDbId": 2,
                "studyDbId": 2,
                "analysisMethod": "GoldenGate",
                "resultCount": 1,
                "germplasmDbId": 4
            }
        ]
    }
}"""
        params = {
            "germplasm": 3
        }
        
        test_post(self, '/brapi/v1/programs-search', params, expected)

    # end def test_post_search
    
# end class MarkerProfilesTest