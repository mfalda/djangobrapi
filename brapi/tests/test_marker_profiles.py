from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class MarkerProfilesTest(APITestCase):
    
    fixtures = ['crops.json', 'programs.json', 'trials.json', 'study_types.json',
                'locations.json', 'studies.json',
                'germplasm.json', 'allele_matrices.json',
                'allele_matrix_search.json', 'marker_profiles.json']
    
    
    def test_get_allele_matrices(self):

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
                "studyDbId": 1001
            },
            {
                "name": "testDs2",
                "matrixDbId": 28,
                "description": "a second test dataset",
                "lastUpdated": "2017-06-12",
                "studyDbId": 1002
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/allelematrices/', expected)
        
    # end def test_get_allele_matrices


    def test_get_allele_matrix_search(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 4,
            "pageSize": 100
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            [
                "1",
                "1",
                "A/B"
            ],
            [
                "1",
                "2",
                "B"
            ],
            [
                "2",
                "1",
                "A"
            ],
            [
                "2",
                "2",
                "A/B"
            ]
        ]
    }
}"""
        test_get(self, '/brapi/v1/allelematrix-search', expected)
        
    # end def test_get_allele_matrix_search
    
    
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
                "germplasmDbId": "3"
            },
            {
                "markerProfilesDbId": 4,
                "uniqueDisplayName": "germplasm4",
                "sampleDbId": 44,
                "extractDbId": 2,
                "studyDbId": 2,
                "analysisMethod": "GoldenGate",
                "resultCount": 1,
                "germplasmDbId": "4"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/markerprofiles', expected)
        
    # end def test_get_markerprofiles


    def test_get_markerprofiles_data(self):

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
                "markerProfilesDbId": 3,
                "uniqueDisplayName": "germplasm3",
                "sampleDbId": 33,
                "extractDbId": 1,
                "studyDbId": 1,
                "analysisMethod": "GBS",
                "resultCount": 1,
                "germplasmDbId": "3"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/markerprofiles/3/', expected)
        
    # end def test_get_markerprofiles_data 
    
    
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
                "markerProfilesDbId": 3,
                "uniqueDisplayName": "germplasm3",
                "sampleDbId": 33,
                "extractDbId": 1,
                "studyDbId": 1,
                "analysisMethod": "GBS",
                "resultCount": 1,
                "germplasmDbId": "3"
            }
        ]
    }
}"""
        params = {
            "germplasm": [3]
        }
        
        test_post(self, '/brapi/v1/markerprofiles', params, expected)

    # end def test_post_search
    
# end class MarkerProfilesTest