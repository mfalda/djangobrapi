from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class AlleleMatrixSearch(APITestCase):
    
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
            "totalPages": 1,
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


    def test_get_allele_matrices_studyDbId(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 1,
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
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/allelematrices/?studyDbId=1001&pageSize=2', expected)

    # end def test_get_allele_matrices_studyDbId


    def test_get_allele_matrix_search_markerprofileDbId(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 2,
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
                    1,
                    1,
                    "A/A"
                ],
                [
                    1,
                    1,
                    "B/B"
                ]
            ]
        ]
    }
}"""
        test_get(self, '/brapi/v1/allelematrix-search/?markerprofileDbId=1&pageSize=2', expected)

    # end def test_get_allele_matrix_search_markerprofileDbId


    def test_get_allele_matrix_search_markerDbId(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 2,
            "totalCount": 4,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
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
            ],
            [
                [
                    3,
                    4,
                    "A|B"
                ],
                [
                    4,
                    4,
                    "A/A"
                ],
                [
                    5,
                    4,
                    "A/A"
                ],
                [
                    1,
                    4,
                    "A/A"
                ],
                [
                    2,
                    4,
                    "B/B"
                ],
                [
                    3,
                    4,
                    "A|B"
                ],
                [
                    4,
                    4,
                    "A|B"
                ],
                [
                    5,
                    4,
                    "A/A"
                ],
                [
                    1,
                    4,
                    "A/A"
                ],
                [
                    2,
                    4,
                    "A/A"
                ],
                [
                    3,
                    4,
                    "B/B"
                ],
                [
                    4,
                    4,
                    "N"
                ]
            ]
        ]
    }
}"""
        test_get(self, '/brapi/v1/allelematrix-search/?markerDbId=2&pageSize=2', expected)

    # end def test_get_allele_matrix_search_markerDbId

    def test_get_allele_matrix_search_matrixDbId(self):

        expected = """{
}"""
        #test_get(self, '/brapi/v1/allelematrix-search/?matrixDbId=1&pageSize=2', expected)
        self.assertJSONEqual("{}", expected)

    # end def test_get_allele_matrix_search_matrixDbId


    def test_post_allele_matrix_search(self):

        expected = """
        {
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 12,
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


    def test_post_allele_matrix_search_markerprofileDbId(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 2,
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
                    1,
                    1,
                    "A/A"
                ],
                [
                    1,
                    1,
                    "B/B"
                ]
            ]
        ]
    }
}"""

        params = {
            "markerprofileDbId": [1],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/allelematrix-search?pageSize=2', params, expected)

    # end def test_post_allele_matrix_search_markerprofileDbId


    def test_post_allele_matrix_search_markerDbId(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 3,
            "totalCount": 6,
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
            "markerDbId": [1],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/allelematrix-search?pageSize=2', params, expected)

    # end def test_post_allele_matrix_search_markerDbId


    def test_post_allele_matrix_search_matrixDbId(self):

        expected = """{
}"""

        params = {
            "matrixDbId": 1,
            "pageSize": 2
        }

        # test_post(self, '/brapi/v1/allelematrix-search?pageSize=2', params, expected)
        self.assertJSONEqual("{}", expected)

    # end def test_post_allele_matrix_search_matrixDbId

# end class AlleleMatrixSearch


class MarkerProfileTest(APITestCase):

    fixtures = ['crops.json', 'programs.json', 'trials.json',
                'study_types.json', 'locations.json', 'studies.json',
                'germplasm.json', 'allele_matrices.json', 'markers.json',
                'markerprofiles.json', 'markerprofiles_data.json']


    def test_get_markerprofiles(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 2,
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


    def test_get_markerprofiles_germplasm(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 2,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "markerprofileDbId": 1,
                "resultCount": 2,
                "sampleDbId": 33,
                "extractDbId": 1,
                "analysisMethod": "GBS",
                "germplasmDbId": "1",
                "uniqueDisplayName": "germplasm3"
            },
            {
                "markerprofileDbId": 2,
                "resultCount": 0,
                "sampleDbId": 44,
                "extractDbId": 2,
                "analysisMethod": "GoldenGate",
                "germplasmDbId": "1",
                "uniqueDisplayName": "germplasm4"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/markerprofiles?germplasm=1&pageSize=2', expected)

    # end def test_get_markerprofiles_germplasm


    def test_get_markerprofiles_studyDbId(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 1,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "markerprofileDbId": 1,
                "sampleDbId": 33,
                "resultCount": 2,
                "extractDbId": 1,
                "uniqueDisplayName": "germplasm3",
                "analysisMethod": "GBS"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/markerprofiles?studyDbId=1001&pageSize=2', expected)

    # end def test_get_markerprofiles_studyDbId


    def test_get_markerprofiles_sample(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
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
                "resultCount": 2,
                "sampleDbId": 33,
                "extractDbId": 1,
                "analysisMethod": "GBS",
                "germplasmDbId": "1",
                "uniqueDisplayName": "germplasm3"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/markerprofiles?sample=33&pageSize=2', expected)

    # end def test_get_markerprofiles_sample


    def test_get_markerprofiles_extract(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
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
                "resultCount": 2,
                "sampleDbId": 33,
                "extractDbId": 1,
                "analysisMethod": "GBS",
                "germplasmDbId": "1",
                "uniqueDisplayName": "germplasm3"
            }
        ]
    }
}
"""

        test_get(self, '/brapi/v1/markerprofiles?extract=1&pageSize=2', expected)

    # end def test_get_markerprofiles_extract


    def test_get_markerprofiles_method(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
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
                "resultCount": 2,
                "sampleDbId": 33,
                "extractDbId": 1,
                "analysisMethod": "GBS",
                "germplasmDbId": "1",
                "uniqueDisplayName": "germplasm3"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/markerprofiles?method=GBS&pageSize=2', expected)

    # end def test_get_markerprofiles_method
    
    
    def test_post_markerprofiles(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 2,
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

    # end def test_post_markerprofiles


    def test_post_markerprofiles_germplasm(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 2,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "markerprofileDbId": 1,
                "sampleDbId": 33,
                "resultCount": 2,
                "extractDbId": 1,
                "uniqueDisplayName": "germplasm3",
                "analysisMethod": "GBS"
            },
            {
                "germplasmDbId": "1",
                "markerprofileDbId": 2,
                "sampleDbId": 44,
                "resultCount": 0,
                "extractDbId": 2,
                "uniqueDisplayName": "germplasm4",
                "analysisMethod": "GoldenGate"
            }
        ]
    }
}"""
        params = {
            "germplasm": 1,
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/markerprofiles?pageSize=2', params, expected)

    # end def test_post_markerprofiles_germplasm


    def test_post_markerprofiles_studyDbId(self):

        expected = """
        {
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 1,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "markerprofileDbId": 1,
                "sampleDbId": 33,
                "resultCount": 2,
                "extractDbId": 1,
                "uniqueDisplayName": "germplasm3",
                "analysisMethod": "GBS"
            }
        ]
    }
}"""
        params = {
            "studyDbId": 1001,
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/markerprofiles?pageSize=2', params, expected)

    # end def test_post_markerprofiles_studyDbId


    def test_post_markerprofiles_sample(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 1,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "markerprofileDbId": 1,
                "sampleDbId": 33,
                "resultCount": 2,
                "extractDbId": 1,
                "uniqueDisplayName": "germplasm3",
                "analysisMethod": "GBS"
            }
        ]
    }
}"""
        params = {
            "sample": 33,
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/markerprofiles?pageSize=2', params, expected)

    # end def test_post_markerprofiles_sample


    def test_post_markerprofiles_extract(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 1,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "markerprofileDbId": 1,
                "sampleDbId": 33,
                "resultCount": 2,
                "extractDbId": 1,
                "uniqueDisplayName": "germplasm3",
                "analysisMethod": "GBS"
            }
        ]
    }
}"""
        params = {
            "extract": 1,
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/markerprofiles?pageSize=2', params, expected)

    # end def test_post_markerprofiles_extract


    def test_post_markerprofiles_method(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 1,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "markerprofileDbId": 1,
                "sampleDbId": 33,
                "resultCount": 2,
                "extractDbId": 1,
                "uniqueDisplayName": "germplasm3",
                "analysisMethod": "GBS"
            }
        ]
    }
}"""
        params = {
            "method": "GBS",
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/markerprofiles?pageSize=2', params, expected)

    # end def test_post_markerprofiles_method


    def test_get_markerprofiles_data(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 1,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": [
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
}"""
        test_get(self, '/brapi/v1/markerprofiles/1/?pageSize=2', expected)

    # end def test_get_markerprofiles_data

# end class MarkerProfileTest