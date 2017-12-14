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
            "pageTotal": 1,
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
                "language": "EN",
                "status": "recommended",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "scientist": "",
                "ontologyName": "Wheat ontology",
                "scale": {
                    "defaultValue": null,
                    "scaleDbId": "CO_334:0100528",
                    "xref": null,
                    "name": "ug/m",
                    "validValues": {
                        "min": 1,
                        "max": 2,
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ]
                    },
                    "datatypeDbId": 2,
                    "decimalPlaces": 0,
                    "datatype": "Categorical"
                },
                "xref": "TL_455:0003001",
                "method": {
                    "description": "",
                    "reference": "",
                    "formula": "",
                    "name": "",
                    "methodDbId": "",
                    "classis": ""
                },
                "observationVariableDbId": "MO_123:100002",
                "institution": "",
                "observationVariableName": "Plant height",
                "trait": {
                    "traitDbId": "1",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "status": "recommended",
                    "mainAbbreviation": "CC",
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "name": "Carotenoid content",
                    "traitId": "CO_334:0100620",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "entity": "root",
                    "defaultValue": "",
                    "classis": "physiological trait"
                },
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "ontologyDbId": "CO_334",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": null,
                "crop": "grape"
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
                "language": "EN",
                "status": "recommended",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "scientist": "",
                "ontologyName": "Wheat ontology",
                "scale": {
                    "defaultValue": null,
                    "scaleDbId": "CO_334:0100528",
                    "xref": null,
                    "name": "ug/m",
                    "validValues": {
                        "min": 1,
                        "max": 2,
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ]
                    },
                    "datatypeDbId": 2,
                    "decimalPlaces": 0,
                    "datatype": "Categorical"
                },
                "xref": "TL_455:0003001",
                "method": {
                    "description": "",
                    "reference": "",
                    "formula": "",
                    "name": "",
                    "methodDbId": "",
                    "classis": ""
                },
                "observationVariableDbId": "MO_123:100002",
                "institution": "",
                "observationVariableName": "Plant height",
                "trait": {
                    "traitDbId": "1",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "status": "recommended",
                    "mainAbbreviation": "CC",
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "name": "Carotenoid content",
                    "traitId": "CO_334:0100620",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "entity": "root",
                    "defaultValue": "",
                    "classis": "physiological trait"
                },
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "ontologyDbId": "CO_334",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "defaultValue": null,
                "crop": "grape"
            },
            {
                "language": "EN",
                "status": "active",
                "submissionTimestamp": "2016-05-14T20:12:09Z",
                "scientist": "",
                "ontologyName": "Rice ontology",
                "scale": {
                    "defaultValue": null,
                    "scaleDbId": "CO_334:0100527",
                    "xref": "0",
                    "name": "kg/g",
                    "validValues": {
                        "min": 1,
                        "max": 3,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    },
                    "datatypeDbId": 1,
                    "decimalPlaces": 2,
                    "datatype": "Numeric"
                },
                "xref": "TL_455:0003005",
                "method": {
                    "description": "",
                    "reference": "",
                    "formula": "",
                    "name": "",
                    "methodDbId": "",
                    "classis": ""
                },
                "observationVariableDbId": "MO_123:100003",
                "institution": "",
                "observationVariableName": "Root weight",
                "trait": {
                    "traitDbId": "1",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "attribute": "carotenoid",
                    "status": "recommended",
                    "mainAbbreviation": "CC",
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "name": "Carotenoid content",
                    "traitId": "CO_334:0100620",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "entity": "root",
                    "defaultValue": "",
                    "classis": "physiological trait"
                },
                "synonyms": [
                    "weight"
                ],
                "ontologyDbId": "CO_335",
                "contextOfUse": [
                    ""
                ],
                "defaultValue": "1",
                "crop": "grape"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/variables/?pageSize=2', expected)

    # end def test_get_variable_list
    
    
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
                "trait": {
                    "mainAbbreviation": "CC",
                    "status": "recommended",
                    "description": "Cassava storage root pulp carotenoid content",
                    "entity": "root",
                    "traitDbId": "1",
                    "name": "Carotenoid content",
                    "classis": "physiological trait",
                    "xref": "TL_455:0003023",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "traitId": "CO_334:0100620",
                    "attribute": "carotenoid",
                    "defaultValue": "",
                    "alternativeAbbreviations": [
                        "CCS"
                    ]
                },
                "status": "recommended",
                "institution": "",
                "scientist": "",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "crop": "grape",
                "xref": "TL_455:0003001",
                "observationVariableDbId": "MO_123:100002",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "scale": {
                    "datatype": "Categorical",
                    "scaleDbId": "CO_334:0100528",
                    "name": "ug/m",
                    "datatypeDbId": 2,
                    "xref": null,
                    "defaultValue": null,
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
                "ontologyName": "Wheat ontology",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "ontologyDbId": "CO_334",
                "method": {
                    "reference": "",
                    "methodDbId": "",
                    "description": "",
                    "name": "",
                    "classis": "",
                    "formula": ""
                },
                "language": "EN",
                "defaultValue": null
            }
        ]
    }
}"""
        params = {
            "names": ["Plant height"],
            "pageSize": 2
        }
        
        test_post(self, '/brapi/v1/variables-search', params, expected)

    # end def test_post_search
              
# end class ObsVariablesTest
