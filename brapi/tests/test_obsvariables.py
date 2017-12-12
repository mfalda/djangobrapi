from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class ObsVariablesTest(APITestCase):

    fixtures = ['crops.json', 'datatypes.json', 'ontologies.json',
                'methods.json', 'scales.json',
                'observation_variables.json', 'traits.json']
    

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
            "pageSize": 100
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "method": {
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "classe": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": "",
                    "reference": ""
                },
                "trait": {
                    "traitDbId": "CO_334:0100620",
                    "name": "Carotenoid content",
                    "classe": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": "carotenoid content measure",
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": "CCS",
                    "entity": "root",
                    "attribute": "carotenoid",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "uniqueDisplayName": "",
                    "extractDbId": null,
                    "markerprofileDbId": null,
                    "analysisMethod": "",
                    "data": ""
                },
                "scale": {
                    "validValues": {
                        "categories": [
                            "1"
                        ],
                        "min": 2,
                        "max": 2
                    },
                    "scaleDbId": "CO_334:0100526",
                    "name": "ug/g",
                    "datatype": "Numeric",
                    "decimalPlaces": "0",
                    "xref": null
                },
                "observationVariableDbId": "CO_334:0100622",
                "name": "caro_spectro",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "synonyms": "Carotenoid content by spectro",
                "contextOfUse": "Trial evaluation; Nursery evaluation",
                "growthStage": "mature",
                "status": "recommended",
                "xref": "TL_455:0003001",
                "institution": null,
                "scientist": null,
                "date": "2016-05-13",
                "language": "EN",
                "crop": "cassava",
                "defaultValue": "2"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/variables/CO_334:0100622/', expected)

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
                "method": {
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "classe": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": "",
                    "reference": ""
                },
                "trait": {
                    "traitDbId": "CO_334:0100620",
                    "name": "Carotenoid content",
                    "classe": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": "carotenoid content measure",
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": "CCS",
                    "entity": "root",
                    "attribute": "carotenoid",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "uniqueDisplayName": "",
                    "extractDbId": null,
                    "markerprofileDbId": null,
                    "analysisMethod": "",
                    "data": ""
                },
                "scale": {
                    "validValues": {
                        "categories": [
                            "1"
                        ],
                        "min": 2,
                        "max": 2
                    },
                    "scaleDbId": "CO_334:0100526",
                    "name": "ug/g",
                    "datatype": "Numeric",
                    "decimalPlaces": "0",
                    "xref": null
                },
                "observationVariableDbId": "CO_334:0100622",
                "name": "caro_spectro",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "synonyms": "Carotenoid content by spectro",
                "contextOfUse": "Trial evaluation; Nursery evaluation",
                "growthStage": "mature",
                "status": "recommended",
                "xref": "TL_455:0003001",
                "institution": null,
                "scientist": null,
                "date": "2016-05-13",
                "language": "EN",
                "crop": "cassava",
                "defaultValue": "2"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/variables?traitClass=physiological%20trait', expected)

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
                "method": {
                    "methodDbId": "CO_334:0010320",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "classe": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "formula": "",
                    "reference": ""
                },
                "trait": {
                    "traitDbId": "CO_334:0100620",
                    "name": "Carotenoid content",
                    "classe": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": "carotenoid content measure",
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": "CCS",
                    "entity": "root",
                    "attribute": "carotenoid",
                    "status": "recommended",
                    "xref": "TL_455:0003023",
                    "uniqueDisplayName": "",
                    "extractDbId": null,
                    "markerprofileDbId": null,
                    "analysisMethod": "",
                    "data": ""
                },
                "scale": {
                    "validValues": {
                        "categories": [
                            "1"
                        ],
                        "min": 2,
                        "max": 2
                    },
                    "scaleDbId": "CO_334:0100526",
                    "name": "ug/g",
                    "datatype": "Numeric",
                    "decimalPlaces": "0",
                    "xref": null
                },
                "observationVariableDbId": "CO_334:0100622",
                "name": "caro_spectro",
                "ontologyDbId": "CO_334",
                "ontologyName": "Cassava",
                "synonyms": "Carotenoid content by spectro",
                "contextOfUse": "Trial evaluation; Nursery evaluation",
                "growthStage": "mature",
                "status": "recommended",
                "xref": "TL_455:0003001",
                "institution": null,
                "scientist": null,
                "date": "2016-05-13",
                "language": "EN",
                "crop": "cassava",
                "defaultValue": "2"
            }
        ]
    }
}"""
        params = {
            "names": ["caro_spectro"]
        }
        
        test_post(self, '/brapi/v1/variables-search', params, expected)

    # end def test_post_search
              
# end class ObsVariablesTest
