from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class ObsVariablesTest(APITestCase):

    fixtures = ['crops.json', 'datatypes.json', 'ontologies.json',
                'methods.json', 'valid_values.json', 'scales.json',
                'traits.json', 'observation_variables.json']
    

    def test_get_datatypes(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 6,
            "pageSize": 100
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            "Numeric",
            "Categorical",
            "Date",
            "Text",
            "Picture",
            "Boolean"
        ]
    }
}"""
    
        test_get(self, '/brapi/v1/variables/datatypes/', expected)

    # end def test_get_datatypes
    
    
    def test_get_variable_details(self):

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
                "institution": "",
                "datatype": "Categorical",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "defaultValue": null,
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "crop": "grape",
                "ontologyName": "Wheat ontology",
                "scale": {
                    "decimalPlaces": 0,
                    "datatype": "Categorical",
                    "defaultValue": null,
                    "name": "ug/m",
                    "scaleDbId": "CO_334:0100528",
                    "datatypeDbId": 2,
                    "xref": null,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2
                    }
                },
                "observationVariableName": "Plant height",
                "xref": "TL_455:0003001",
                "language": "EN",
                "ontologyDbId": "CO_334",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "status": "recommended",
                "growthStage": "mature",
                "method": {
                    "formula": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null,
                    "methodDbId": "CO_334:0010320",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "classis": "Estimation"
                },
                "scientist": "",
                "trait": {
                    "traitDbId": "1",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "defaultValue": "",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitId": "CO_334:0100620",
                    "status": "recommended",
                    "entity": "root",
                    "classis": "physiological trait",
                    "attribute": "carotenoid"
                },
                "observationVariableDbId": "MO_123:100002"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/variables/MO_123:100002/?pageSize=2', expected)

    # end def test_get_variable_details
    
     
    def test_get_ontologies(self):

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
                "license": "CC BY-SA 4.0",
                "authors": "J. Snow, H. Peterson",
                "description": "developped for European genetic studies projects",
                "ontologyDbId": "CO_334",
                "copyright": "© 2016, INRA",
                "ontologyName": "Wheat ontology",
                "version": "v1.2"
            },
            {
                "license": null,
                "authors": "J. Doe",
                "description": "developped for IRRI and amended with partners needs",
                "ontologyDbId": "CO_335",
                "copyright": null,
                "ontologyName": "Rice ontology",
                "version": "v2"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/ontologies/?pageSize=2', expected)

    # end def test_get_ontologies
        
    
    def test_get_variable_list(self):

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
                "institution": "",
                "datatype": "Categorical",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "defaultValue": null,
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "crop": "grape",
                "ontologyName": "Wheat ontology",
                "scale": {
                    "decimalPlaces": 0,
                    "datatype": "Categorical",
                    "defaultValue": null,
                    "name": "ug/m",
                    "scaleDbId": "CO_334:0100528",
                    "datatypeDbId": 2,
                    "xref": null,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2
                    }
                },
                "observationVariableName": "Plant height",
                "xref": "TL_455:0003001",
                "language": "EN",
                "ontologyDbId": "CO_334",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "status": "recommended",
                "growthStage": "mature",
                "method": {
                    "formula": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null,
                    "methodDbId": "CO_334:0010320",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "classis": "Estimation"
                },
                "scientist": "",
                "trait": {
                    "traitDbId": "1",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "defaultValue": "",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitId": "CO_334:0100620",
                    "status": "recommended",
                    "entity": "root",
                    "classis": "physiological trait",
                    "attribute": "carotenoid"
                },
                "observationVariableDbId": "MO_123:100002"
            },
            {
                "institution": "",
                "datatype": "Numeric",
                "synonyms": [
                    "weight"
                ],
                "defaultValue": "1",
                "contextOfUse": [
                    ""
                ],
                "crop": "grape",
                "ontologyName": "Rice ontology",
                "scale": {
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "defaultValue": null,
                    "name": "kg/g",
                    "scaleDbId": "CO_334:0100527",
                    "datatypeDbId": 1,
                    "xref": "0",
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    }
                },
                "observationVariableName": "Root weight",
                "xref": "TL_455:0003005",
                "language": "EN",
                "ontologyDbId": "CO_335",
                "submissionTimestamp": "2016-05-14T20:12:09Z",
                "status": "active",
                "growthStage": "ripen",
                "method": null,
                "scientist": "",
                "trait": {
                    "traitDbId": "1",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "defaultValue": "",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitId": "CO_334:0100620",
                    "status": "recommended",
                    "entity": "root",
                    "classis": "physiological trait",
                    "attribute": "carotenoid"
                },
                "observationVariableDbId": "MO_123:100003"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/variables/?pageSize=2', expected)

    # end def test_get_variable_list


    def test_get_variable_list_traitClass(self):

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
                "institution": "",
                "datatype": "Categorical",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "defaultValue": null,
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "crop": "grape",
                "ontologyName": "Wheat ontology",
                "scale": {
                    "decimalPlaces": 0,
                    "datatype": "Categorical",
                    "defaultValue": null,
                    "name": "ug/m",
                    "scaleDbId": "CO_334:0100528",
                    "datatypeDbId": 2,
                    "xref": null,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2
                    }
                },
                "observationVariableName": "Plant height",
                "xref": "TL_455:0003001",
                "language": "EN",
                "ontologyDbId": "CO_334",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "status": "recommended",
                "growthStage": "mature",
                "method": {
                    "formula": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null,
                    "methodDbId": "CO_334:0010320",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "classis": "Estimation"
                },
                "scientist": "",
                "trait": {
                    "traitDbId": "1",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "defaultValue": "",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitId": "CO_334:0100620",
                    "status": "recommended",
                    "entity": "root",
                    "classis": "physiological trait",
                    "attribute": "carotenoid"
                },
                "observationVariableDbId": "MO_123:100002"
            },
            {
                "institution": "",
                "datatype": "Numeric",
                "synonyms": [
                    "weight"
                ],
                "defaultValue": "1",
                "contextOfUse": [
                    ""
                ],
                "crop": "grape",
                "ontologyName": "Rice ontology",
                "scale": {
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "defaultValue": null,
                    "name": "kg/g",
                    "scaleDbId": "CO_334:0100527",
                    "datatypeDbId": 1,
                    "xref": "0",
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    }
                },
                "observationVariableName": "Root weight",
                "xref": "TL_455:0003005",
                "language": "EN",
                "ontologyDbId": "CO_335",
                "submissionTimestamp": "2016-05-14T20:12:09Z",
                "status": "active",
                "growthStage": "ripen",
                "method": null,
                "scientist": "",
                "trait": {
                    "traitDbId": "1",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "defaultValue": "",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitId": "CO_334:0100620",
                    "status": "recommended",
                    "entity": "root",
                    "classis": "physiological trait",
                    "attribute": "carotenoid"
                },
                "observationVariableDbId": "MO_123:100003"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/variables/?traitClass=physiological trait&pageSize=2', expected)

    # end def test_get_variable_list_traitClass

# end class ObsVariablesTest


class ObsVariablesSearchTest(APITestCase):

    fixtures = ['crops.json', 'datatypes.json', 'ontologies.json',
                'methods.json', 'valid_values.json', 'scales.json',
                'traits.json', 'observation_variables.json']


    def test_post_variables_search(self):

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
                "institution": "",
                "datatype": "Categorical",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "defaultValue": null,
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "crop": "grape",
                "ontologyName": "Wheat ontology",
                "scale": {
                    "decimalPlaces": 0,
                    "datatype": "Categorical",
                    "defaultValue": null,
                    "name": "ug/m",
                    "scaleDbId": "CO_334:0100528",
                    "datatypeDbId": 2,
                    "xref": null,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2
                    }
                },
                "observationVariableName": "Plant height",
                "xref": "TL_455:0003001",
                "language": "EN",
                "ontologyDbId": "CO_334",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "status": "recommended",
                "growthStage": "mature",
                "method": {
                    "formula": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null,
                    "methodDbId": "CO_334:0010320",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "classis": "Estimation"
                },
                "scientist": "",
                "trait": {
                    "traitDbId": "1",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "defaultValue": "",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitId": "CO_334:0100620",
                    "status": "recommended",
                    "entity": "root",
                    "classis": "physiological trait",
                    "attribute": "carotenoid"
                },
                "observationVariableDbId": "MO_123:100002"
            },
            {
                "institution": "",
                "datatype": "Numeric",
                "synonyms": [
                    "weight"
                ],
                "defaultValue": "1",
                "contextOfUse": [
                    ""
                ],
                "crop": "grape",
                "ontologyName": "Rice ontology",
                "scale": {
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "defaultValue": null,
                    "name": "kg/g",
                    "scaleDbId": "CO_334:0100527",
                    "datatypeDbId": 1,
                    "xref": "0",
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3
                    }
                },
                "observationVariableName": "Root weight",
                "xref": "TL_455:0003005",
                "language": "EN",
                "ontologyDbId": "CO_335",
                "submissionTimestamp": "2016-05-14T20:12:09Z",
                "status": "active",
                "growthStage": "ripen",
                "method": null,
                "scientist": "",
                "trait": {
                    "traitDbId": "1",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "defaultValue": "",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitId": "CO_334:0100620",
                    "status": "recommended",
                    "entity": "root",
                    "classis": "physiological trait",
                    "attribute": "carotenoid"
                },
                "observationVariableDbId": "MO_123:100003"
            }
        ]
    }
}"""
        params = {
            "pageSize": 2
        }
        
        test_post(self, '/brapi/v1/variables-search?pageSize=2', params, expected)

    # end def test_post_variables_search


    def test_post_variables_search_observationVariableDbIds(self):

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
                "growthStage": "mature",
                "defaultValue": null,
                "language": "EN",
                "ontologyDbId": "CO_334",
                "observationVariableName": "Plant height",
                "xref": "TL_455:0003001",
                "institution": "",
                "scientist": "",
                "datatype": "Categorical",
                "status": "recommended",
                "crop": "grape",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "trait": {
                    "defaultValue": "",
                    "traitId": "CO_334:0100620",
                    "mainAbbreviation": "CC",
                    "xref": "TL_455:0003023",
                    "traitDbId": "1",
                    "name": "Carotenoid content",
                    "status": "recommended",
                    "classis": "physiological trait",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "attribute": "carotenoid",
                    "entity": "root",
                    "description": "Cassava storage root pulp carotenoid content",
                    "alternativeAbbreviations": [
                        "CCS"
                    ]
                },
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "classis": "Estimation",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
                },
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "ontologyName": "Wheat ontology",
                "observationVariableDbId": "MO_123:100002",
                "scale": {
                    "defaultValue": null,
                    "xref": null,
                    "name": "ug/m",
                    "datatype": "Categorical",
                    "scaleDbId": "CO_334:0100528",
                    "validValues": {
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2,
                        "min": 1
                    },
                    "datatypeDbId": 2,
                    "decimalPlaces": 0
                }
            }
        ]
    }
}"""

        params = {
            "observationVariableDbIds": ["MO_123:100002"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/variables-search?pageSize=2', params, expected)

    # end def test_post_variables_search_observationVariableDbIds


    def test_post_variables_search_ontologyXrefs(self):

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
                "trait": {
                    "name": "Carotenoid content",
                    "entity": "root",
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "traitId": "CO_334:0100620",
                    "xref": "TL_455:0003023",
                    "attribute": "carotenoid",
                    "traitDbId": "1",
                    "status": "recommended",
                    "defaultValue": "",
                    "classis": "physiological trait"
                },
                "ontologyName": "Wheat ontology",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "methodDbId": "CO_334:0010320",
                    "classis": "Estimation",
                    "formula": null
                },
                "observationVariableDbId": "MO_123:100002",
                "ontologyDbId": "CO_334",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "institution": "",
                "xref": "TL_455:0003001",
                "language": "EN",
                "defaultValue": null,
                "datatype": "Categorical",
                "status": "recommended",
                "observationVariableName": "Plant height",
                "crop": "grape",
                "scientist": "",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "scale": {
                    "name": "ug/m",
                    "scaleDbId": "CO_334:0100528",
                    "validValues": {
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2,
                        "min": 1
                    },
                    "datatypeDbId": 2,
                    "decimalPlaces": 0,
                    "xref": null,
                    "datatype": "Categorical",
                    "defaultValue": null
                },
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "mature"
            },
            {
                "trait": {
                    "name": "Plant height",
                    "entity": "trunk",
                    "mainAbbreviation": "HM",
                    "alternativeAbbreviations": [
                        "PHM"
                    ],
                    "description": "Cassava marketable yield",
                    "synonyms": [
                        "height measure"
                    ],
                    "traitId": "CO_334:0100621",
                    "xref": "TL_455:0003024",
                    "attribute": "height",
                    "traitDbId": "2",
                    "status": "accepted",
                    "defaultValue": "",
                    "classis": "physiological trait"
                },
                "ontologyName": "Wheat ontology",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "methodDbId": "CO_334:0010320",
                    "classis": "Estimation",
                    "formula": null
                },
                "observationVariableDbId": "MO_123:100004",
                "ontologyDbId": "CO_334",
                "synonyms": [
                    "color"
                ],
                "institution": "",
                "xref": "TL_455:0003001",
                "language": "FR",
                "defaultValue": null,
                "datatype": "Numeric",
                "status": "recommended",
                "observationVariableName": "Root color",
                "crop": "grape",
                "scientist": "",
                "submissionTimestamp": "2016-05-13T20:06:09Z",
                "scale": {
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "datatypeDbId": 1,
                    "decimalPlaces": 3,
                    "xref": null,
                    "datatype": "Numeric",
                    "defaultValue": ""
                },
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "embryon"
            }
        ]
    }
}"""

        params = {
            "ontologyXrefs": ["TL_455:0003001"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/variables-search?pageSize=2', params, expected)

    # end def test_post_variables_search_ontologyXrefs


    def test_post_variables_search_ontologyDbIds(self):

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
                "trait": {
                    "name": "Carotenoid content",
                    "entity": "root",
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "traitId": "CO_334:0100620",
                    "xref": "TL_455:0003023",
                    "attribute": "carotenoid",
                    "traitDbId": "1",
                    "status": "recommended",
                    "defaultValue": "",
                    "classis": "physiological trait"
                },
                "ontologyName": "Wheat ontology",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "methodDbId": "CO_334:0010320",
                    "classis": "Estimation",
                    "formula": null
                },
                "observationVariableDbId": "MO_123:100002",
                "ontologyDbId": "CO_334",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "institution": "",
                "xref": "TL_455:0003001",
                "language": "EN",
                "defaultValue": null,
                "datatype": "Categorical",
                "status": "recommended",
                "observationVariableName": "Plant height",
                "crop": "grape",
                "scientist": "",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "scale": {
                    "name": "ug/m",
                    "scaleDbId": "CO_334:0100528",
                    "validValues": {
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2,
                        "min": 1
                    },
                    "datatypeDbId": 2,
                    "decimalPlaces": 0,
                    "xref": null,
                    "datatype": "Categorical",
                    "defaultValue": null
                },
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "mature"
            },
            {
                "trait": {
                    "name": "Plant height",
                    "entity": "trunk",
                    "mainAbbreviation": "HM",
                    "alternativeAbbreviations": [
                        "PHM"
                    ],
                    "description": "Cassava marketable yield",
                    "synonyms": [
                        "height measure"
                    ],
                    "traitId": "CO_334:0100621",
                    "xref": "TL_455:0003024",
                    "attribute": "height",
                    "traitDbId": "2",
                    "status": "accepted",
                    "defaultValue": "",
                    "classis": "physiological trait"
                },
                "ontologyName": "Wheat ontology",
                "method": {
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "methodDbId": "CO_334:0010320",
                    "classis": "Estimation",
                    "formula": null
                },
                "observationVariableDbId": "MO_123:100004",
                "ontologyDbId": "CO_334",
                "synonyms": [
                    "color"
                ],
                "institution": "",
                "xref": "TL_455:0003001",
                "language": "FR",
                "defaultValue": null,
                "datatype": "Numeric",
                "status": "recommended",
                "observationVariableName": "Root color",
                "crop": "grape",
                "scientist": "",
                "submissionTimestamp": "2016-05-13T20:06:09Z",
                "scale": {
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526",
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "datatypeDbId": 1,
                    "decimalPlaces": 3,
                    "xref": null,
                    "datatype": "Numeric",
                    "defaultValue": ""
                },
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "growthStage": "embryon"
            }
        ]
    }
}"""

        params = {
            "ontologyDbIds": ["CO_334"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/variables-search?pageSize=2', params, expected)

    # end def test_post_variables_search_ontologyDbIds


    def test_post_variables_search_methodDbIds(self):

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
                "method": {
                    "formula": null,
                    "classis": "Estimation",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320"
                },
                "institution": "",
                "scientist": "",
                "observationVariableDbId": "MO_123:100002",
                "xref": "TL_455:0003001",
                "crop": "grape",
                "status": "recommended",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": null,
                "language": "EN",
                "scale": {
                    "xref": null,
                    "datatypeDbId": 2,
                    "defaultValue": null,
                    "datatype": "Categorical",
                    "decimalPlaces": 0,
                    "validValues": {
                        "max": 2,
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "min": 1
                    },
                    "name": "ug/m",
                    "scaleDbId": "CO_334:0100528"
                },
                "ontologyName": "Wheat ontology",
                "datatype": "Categorical",
                "trait": {
                    "attribute": "carotenoid",
                    "classis": "physiological trait",
                    "traitDbId": "1",
                    "mainAbbreviation": "CC",
                    "xref": "TL_455:0003023",
                    "status": "recommended",
                    "description": "Cassava storage root pulp carotenoid content",
                    "entity": "root",
                    "defaultValue": "",
                    "traitId": "CO_334:0100620",
                    "name": "Carotenoid content",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "synonyms": [
                        "carotenoid content measure"
                    ]
                },
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "ontologyDbId": "CO_334",
                "growthStage": "mature",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "observationVariableName": "Plant height"
            },
            {
                "method": {
                    "formula": null,
                    "classis": "Estimation",
                    "reference": null,
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320"
                },
                "institution": "",
                "scientist": "",
                "observationVariableDbId": "MO_123:100004",
                "xref": "TL_455:0003001",
                "crop": "grape",
                "status": "recommended",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": null,
                "language": "FR",
                "scale": {
                    "xref": null,
                    "datatypeDbId": 1,
                    "defaultValue": "",
                    "datatype": "Numeric",
                    "decimalPlaces": 3,
                    "validValues": {
                        "max": 3,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "min": 1
                    },
                    "name": "ug/g",
                    "scaleDbId": "CO_334:0100526"
                },
                "ontologyName": "Wheat ontology",
                "datatype": "Numeric",
                "trait": {
                    "attribute": "height",
                    "classis": "physiological trait",
                    "traitDbId": "2",
                    "mainAbbreviation": "HM",
                    "xref": "TL_455:0003024",
                    "status": "accepted",
                    "description": "Cassava marketable yield",
                    "entity": "trunk",
                    "defaultValue": "",
                    "traitId": "CO_334:0100621",
                    "name": "Plant height",
                    "alternativeAbbreviations": [
                        "PHM"
                    ],
                    "synonyms": [
                        "height measure"
                    ]
                },
                "submissionTimestamp": "2016-05-13T20:06:09Z",
                "ontologyDbId": "CO_334",
                "growthStage": "embryon",
                "synonyms": [
                    "color"
                ],
                "observationVariableName": "Root color"
            }
        ]
    }
}"""

        params = {
            "methodDbIds": ["CO_334:0010320"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/variables-search?pageSize=2', params, expected)

    # end def test_post_variables_search_methodDbIds


    def test_post_variables_search_scaleDbIds(self):

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
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "ontologyName": "Wheat ontology",
                "crop": "grape",
                "datatype": "Categorical",
                "institution": "",
                "status": "recommended",
                "ontologyDbId": "CO_334",
                "scale": {
                    "datatype": "Categorical",
                    "decimalPlaces": 0,
                    "validValues": {
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2,
                        "min": 1
                    },
                    "datatypeDbId": 2,
                    "xref": null,
                    "scaleDbId": "CO_334:0100528",
                    "name": "ug/m",
                    "defaultValue": null
                },
                "observationVariableName": "Plant height",
                "observationVariableDbId": "MO_123:100002",
                "scientist": "",
                "language": "EN",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "xref": "TL_455:0003001",
                "growthStage": "mature",
                "trait": {
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "mainAbbreviation": "CC",
                    "status": "recommended",
                    "classis": "physiological trait",
                    "entity": "root",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitId": "CO_334:0100620",
                    "traitDbId": "1",
                    "xref": "TL_455:0003023",
                    "name": "Carotenoid content",
                    "defaultValue": ""
                },
                "method": {
                    "reference": null,
                    "formula": null,
                    "classis": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "methodDbId": "CO_334:0010320"
                },
                "defaultValue": null
            }
        ]
    }
}"""

        params = {
            "scaleDbIds": ["CO_334:0100528"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/variables-search?pageSize=2', params, expected)

    # end def test_post_variables_search_scaleDbIds


    def test_post_variables_search_names(self):

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
                "synonyms": [
                    "weight"
                ],
                "submissionTimestamp": "2016-05-14T20:12:09Z",
                "ontologyName": "Rice ontology",
                "crop": "grape",
                "datatype": "Numeric",
                "institution": "",
                "status": "active",
                "ontologyDbId": "CO_335",
                "scale": {
                    "datatype": "Numeric",
                    "decimalPlaces": 2,
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "datatypeDbId": 1,
                    "xref": "0",
                    "scaleDbId": "CO_334:0100527",
                    "name": "kg/g",
                    "defaultValue": null
                },
                "observationVariableName": "Root weight",
                "observationVariableDbId": "MO_123:100003",
                "scientist": "",
                "language": "EN",
                "contextOfUse": [
                    ""
                ],
                "xref": "TL_455:0003005",
                "growthStage": "ripen",
                "trait": {
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "mainAbbreviation": "CC",
                    "status": "recommended",
                    "classis": "physiological trait",
                    "entity": "root",
                    "description": "Cassava storage root pulp carotenoid content",
                    "traitId": "CO_334:0100620",
                    "traitDbId": "1",
                    "xref": "TL_455:0003023",
                    "name": "Carotenoid content",
                    "defaultValue": ""
                },
                "method": null,
                "defaultValue": "1"
            }
        ]
    }
}"""

        params = {
            "names": ["Root weight"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/variables-search?pageSize=2', params, expected)

    # end def test_post_variables_search_names


    def test_post_variables_search_datatypes(self):

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
                "trait": {
                    "traitDbId": "1",
                    "entity": "root",
                    "traitId": "CO_334:0100620",
                    "description": "Cassava storage root pulp carotenoid content",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "defaultValue": "",
                    "mainAbbreviation": "CC",
                    "name": "Carotenoid content",
                    "attribute": "carotenoid",
                    "classis": "physiological trait"
                },
                "method": {
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "methodDbId": "CO_334:0010320",
                    "formula": null,
                    "reference": null,
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "classis": "Estimation"
                },
                "observationVariableName": "Plant height",
                "status": "recommended",
                "xref": "TL_455:0003001",
                "language": "EN",
                "scale": {
                    "decimalPlaces": 0,
                    "xref": null,
                    "validValues": {
                        "min": 1,
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2
                    },
                    "datatypeDbId": 2,
                    "datatype": "Categorical",
                    "defaultValue": null,
                    "scaleDbId": "CO_334:0100528",
                    "name": "ug/m"
                },
                "institution": "",
                "observationVariableDbId": "MO_123:100002",
                "growthStage": "mature",
                "ontologyDbId": "CO_334",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "datatype": "Categorical",
                "scientist": "",
                "defaultValue": null,
                "crop": "grape",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "ontologyName": "Wheat ontology"
            }
        ]
    }
}"""

        params = {
            "datatypes": ["Categorical"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/variables-search?pageSize=2', params, expected)

    # end def test_post_variables_search_datatypes


    def test_post_variables_search_traitClasses(self):

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
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "language": "EN",
                "crop": "grape",
                "growthStage": "mature",
                "observationVariableDbId": "MO_123:100002",
                "institution": "",
                "ontologyName": "Wheat ontology",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "scale": {
                    "name": "ug/m",
                    "datatypeDbId": 2,
                    "scaleDbId": "CO_334:0100528",
                    "xref": null,
                    "defaultValue": null,
                    "datatype": "Categorical",
                    "decimalPlaces": 0,
                    "validValues": {
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2,
                        "min": 1
                    }
                },
                "observationVariableName": "Plant height",
                "scientist": "",
                "xref": "TL_455:0003001",
                "defaultValue": null,
                "trait": {
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "mainAbbreviation": "CC",
                    "classis": "physiological trait",
                    "traitDbId": "1",
                    "entity": "root",
                    "traitId": "CO_334:0100620",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "defaultValue": "",
                    "description": "Cassava storage root pulp carotenoid content",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "attribute": "carotenoid"
                },
                "datatype": "Categorical",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "method": {
                    "classis": "Estimation",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "formula": null,
                    "methodDbId": "CO_334:0010320",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "reference": null
                },
                "ontologyDbId": "CO_334",
                "status": "recommended"
            },
            {
                "synonyms": [
                    "weight"
                ],
                "language": "EN",
                "crop": "grape",
                "growthStage": "ripen",
                "observationVariableDbId": "MO_123:100003",
                "institution": "",
                "ontologyName": "Rice ontology",
                "contextOfUse": [
                    ""
                ],
                "scale": {
                    "name": "kg/g",
                    "datatypeDbId": 1,
                    "scaleDbId": "CO_334:0100527",
                    "xref": "0",
                    "defaultValue": null,
                    "datatype": "Numeric",
                    "decimalPlaces": 2,
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    }
                },
                "observationVariableName": "Root weight",
                "scientist": "",
                "xref": "TL_455:0003005",
                "defaultValue": "1",
                "trait": {
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "mainAbbreviation": "CC",
                    "classis": "physiological trait",
                    "traitDbId": "1",
                    "entity": "root",
                    "traitId": "CO_334:0100620",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "defaultValue": "",
                    "description": "Cassava storage root pulp carotenoid content",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "attribute": "carotenoid"
                },
                "datatype": "Numeric",
                "submissionTimestamp": "2016-05-14T20:12:09Z",
                "method": null,
                "ontologyDbId": "CO_335",
                "status": "active"
            }
        ]
    }
}"""

        params = {
            "traitClasses": ["physiological trait"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/variables-search?pageSize=2', params, expected)

    # end def test_post_variables_search_traitClasses

# end class ObsVariablesSearchTest
