from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class MarkerProfileTest(APITestCase):
    
    fixtures = ['crops.json', 'programs.json', 'trials.json',
                'study_types.json', 'locations.json', 'studies.json',
                'germplasm.json', 'allele_matrices.json', 'markers.json',
                'markerprofiles.json', 'markerprofiles_data.json']
    
    
    def test_get_allele_matrices(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 2,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "matrixDbId": 27,
                "name": "testDs1",
                "description": "a test dataset",
                "lastUpdated": "2017-06-12",
                "studyDbId": 1001
            },
            {
                "matrixDbId": 28,
                "name": "testDs2",
                "description": "a second test dataset",
                "lastUpdated": "2017-06-12",
                "studyDbId": 1002
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/allelematrices/?pageSize=2', expected)

    # end def test_get_allele_matrices


    def test_get_allele_matrix_search(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 12,
            "totalCount": 24,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            [
                [
                    1,
                    1,
                    "A/A"
                ],
                [
                    1,
                    1,
                    "B/B"
                ]
            ],
            [
                [
                    5,
                    3,
                    "A/A"
                ],
                [
                    1,
                    3,
                    "B/B"
                ],
                [
                    2,
                    3,
                    "A|B"
                ],
                [
                    3,
                    3,
                    "A|B"
                ],
                [
                    4,
                    3,
                    "A|B"
                ],
                [
                    5,
                    3,
                    "A/A"
                ],
                [
                    1,
                    3,
                    "A/A"
                ],
                [
                    2,
                    3,
                    "A/A"
                ],
                [
                    3,
                    3,
                    "B/B"
                ],
                [
                    4,
                    3,
                    "N"
                ]
            ]
        ]
    }
}"""
        test_get(self, '/brapi/v1/allelematrix-search/?pageSize=2', expected)

    # end def test_get_allele_matrix_search


    def test_post_allele_matrix_search(self):

        expected = """
        {
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 12,
            "totalCount": 24,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            [
                [
                    1,
                    1,
                    "A/A"
                ],
                [
                    1,
                    1,
                    "B/B"
                ]
            ],
            [
                [
                    5,
                    3,
                    "A/A"
                ],
                [
                    1,
                    3,
                    "B/B"
                ],
                [
                    2,
                    3,
                    "A|B"
                ],
                [
                    3,
                    3,
                    "A|B"
                ],
                [
                    4,
                    3,
                    "A|B"
                ],
                [
                    5,
                    3,
                    "A/A"
                ],
                [
                    1,
                    3,
                    "A/A"
                ],
                [
                    2,
                    3,
                    "A/A"
                ],
                [
                    3,
                    3,
                    "B/B"
                ],
                [
                    4,
                    3,
                    "N"
                ]
            ]
        ]
    }
}"""

        params = {
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/allelematrix-search?pageSize=2', params, expected)

    # end def test_post_allele_matrix_search


    def test_get_markerprofiles(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 4,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "analysisMethod": "GBS",
                "resultCount": 2,
                "sampleDbId": 33,
                "uniqueDisplayName": "germplasm3",
                "markerprofileDbId": 1,
                "germplasmDbId": "1",
                "extractDbId": 1
            },
            {
                "analysisMethod": "GoldenGate",
                "resultCount": 0,
                "sampleDbId": 44,
                "uniqueDisplayName": "germplasm4",
                "markerprofileDbId": 2,
                "germplasmDbId": "1",
                "extractDbId": 2
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/markerprofiles/?pageSize=2', expected)
        
    # end def test_get_markerprofiles

    
    def test_post_search(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 4,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "analysisMethod": "GBS",
                "resultCount": 2,
                "sampleDbId": 33,
                "uniqueDisplayName": "germplasm3",
                "markerprofileDbId": 1,
                "germplasmDbId": "1",
                "extractDbId": 1
            },
            {
                "analysisMethod": "GoldenGate",
                "resultCount": 0,
                "sampleDbId": 44,
                "uniqueDisplayName": "germplasm4",
                "markerprofileDbId": 2,
                "germplasmDbId": "1",
                "extractDbId": 2
            }
        ]
    }
}"""
        params = {
            "pageSize": 2
        }
        
        test_post(self, '/brapi/v1/markerprofiles?pageSize=2', params, expected)

    # end def test_post_search


    def test_get_markerprofiles_data(self):

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
                "markerprofileDbId": 1,
                "data": [
                    {
                        "a_01_10001": "A/A"
                    },
                    {
                        "a_01_10001": "B/B"
                    }
                ],
                "uniqueDisplayName": "germplasm3",
                "extractDbId": 1,
                "analysisMethod": "GBS",
                "germplasmDbId": "1"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/markerprofiles/1/?pageSize=2', expected)

    # end def test_get_markerprofiles_data

# end class MarkerProfileTest