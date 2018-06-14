from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class MarkerTest(APITestCase):
    
    fixtures = ['crops.json', 'markers.json']


    def test_get_markers(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 3,
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


    def test_get_markers_name(self):

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
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/markers/?name=a_01_10001&pageSize=2', expected)

        # end def test_get_markers_name


    def test_get_markers_type(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            },
            {
                "markerDbId": 2,
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
                ],
                "defaultDisplayName": "A_01_10002",
                "type": "SNP"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/markers/?type=SNP&pageSize=2', expected)

    # end def test_get_markers_type


    def test_get_markers_caseIns(self):

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
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/markers/?name=A_01_10001&matchMethod=case_insensitive&pageSize=2', expected)

    # end def test_get_markers_caseIns

    def test_get_markers_wildcard(self):

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
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            },
            {
                "markerDbId": 2,
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
                ],
                "defaultDisplayName": "A_01_10002",
                "type": "SNP"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/markers/?name=A_01*&matchMethod=wildcard&pageSize=2', expected)

    # end def test_get_markers_wildcard


    def test_get_markers_synonyms(self):

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
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/markers/?name=popA_10001&include=synonyms&pageSize=2', expected)

    # end def test_get_markers_synonyms


    def test_post_markers(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 3,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            },
            {
                "markerDbId": 2,
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
                ],
                "defaultDisplayName": "A_01_10002",
                "type": "SNP"
            }
        ]
    }
}"""

        params = {}

        test_post(self, '/brapi/v1/markers/?pageSize=2', params, expected)

    # end def test_post_markers


    def test_post_markers_markerDbIds(self):

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
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            },
            {
                "markerDbId": 2,
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
                ],
                "defaultDisplayName": "A_01_10002",
                "type": "SNP"
            }
        ]
    }
}"""

        params = {
            "markerDbIds": [1, 2]
        }

        test_post(self, '/brapi/v1/markers/?pageSize=2', params, expected)

    # end def test_post_markers_markerDbIds


    def test_post_markers_name(self):

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
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            }
        ]
    }
}"""

        params = {
            "name": "a_01_10001"
        }

        test_post(self, '/brapi/v1/markers/?pageSize=2', params, expected)

        # end def test_post_markers_name


    def test_post_markers_type(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            },
            {
                "markerDbId": 2,
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
                ],
                "defaultDisplayName": "A_01_10002",
                "type": "SNP"
            }
        ]
    }
}"""

        params = {
            "type": ["SNP"]
        }

        test_post(self, '/brapi/v1/markers/?pageSize=2', params, expected)

    # end def test_post_markers_type


    def test_post_markers_caseIns(self):

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
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            }
        ]
    }
}"""

        params = {
            "name": "A_01_10001",
            "matchMethod": "case_insensitive"
        }

        test_post(self, '/brapi/v1/markers/?pageSize=2', params, expected)

    # end def test_post_markers_caseIns


    def test_post_markers_wildcard(self):

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
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            },
            {
                "markerDbId": 2,
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
                ],
                "defaultDisplayName": "A_01_10002",
                "type": "SNP"
            }
        ]
    }
}"""

        params = {
            "name": "A_01*",
            "matchMethod": "wildcard"
        }

        test_post(self, '/brapi/v1/markers/?pageSize=2', params, expected)

    # end def test_post_markers_wildcard


    def test_post_markers_synonyms(self):

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
                "markerDbId": 1,
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
                ],
                "defaultDisplayName": "a_01_10001",
                "type": "SNP"
            }
        ]
    }
}"""

        params = {
            "name": "popA_10001",
            "includeSynonyms": "synonyms"
        }

        test_post(self, '/brapi/v1/markers/?pageSize=2', params, expected)

    # end def test_post_markers_synonyms
    
    
    def test_get_marker_details(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
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
