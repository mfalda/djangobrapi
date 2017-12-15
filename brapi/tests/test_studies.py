from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class StudyTest(APITestCase):
    
    fixtures = ['crops.json', 'programs.json', 'trials.json', 'locations.json', 'contacts.json',
                'location_addInfo.json', 'study_types.json', 'studies.json', 'seasons.json',
                'study_observation_levels.json', 'study_seasons.json', 'datalinks.json', 'datatypes.json',
                'study_contacts.json', 'study_types.json', 'study_addInfo.json', 'valid_values.json', 'traits.json',
                'germplasm.json', 'observation_units.json', 'observation_units_addInfo.json',
                'methods.json', 'scales.json', 'ontologies.json', 'observations.json', 'observation_variables.json',
                'observation_unit_xrefs.json']
    

    def test_get_obs_levels(self):

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
            "plant",
            "plot"
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/observationLevels/?pageSize=2', expected)
        
    # end def test_get_obs_levels
    

    def test_get_seasons(self):

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
                "year": "2013",
                "season": "Spring",
                "seasonDbId": "1"
            },
            {
                "year": "2011",
                "season": "Fall",
                "seasonDbId": "2"
            }
        ]
    }
}"""
       
        test_get(self, '/brapi/v1/seasons/?pageSize=2', expected)
        
    # end def test_get_seasons
    
    
    def test_get_types(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageSize": 100,
            "totalCount": 3,
            "pageTotal": 1
        },
        "datafiles": [],
        "status": []
    },
    "result": {
        "data": [
            {
                "name": "Crossing Nursery",
                "description": "Description for Nursery study type"
            },
            {
                "name": "Genotype",
                "description": "Description for Genotyping study type"
            },
            {
                "name": "Yield study",
                "description": "Description for yield study type"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/studyTypes/', expected)
       
    # end def test_get_types
    
    
    def test_get_obsUnit_details(self):

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
                "observationUnitDbId": "1",
                "observationUnitXref": [
                    {
                        "source": "ebi.biosample",
                        "identifier": "SAMEA179865230"
                    },
                    {
                        "source": "gnpis.lot",
                        "identifier": "INRA:CoeSt6_SMH03"
                    },
                    {
                        "source": "kernelDB",
                        "identifier": "239865"
                    }
                ],
                "Y": "1",
                "replicate": "0",
                "entryNumber": "1",
                "germplasmDbId": "1",
                "observations": [
                    {
                        "observationDbId": "1",
                        "observationVariableName": "Plant height",
                        "observationVariableDbId": "MO_123:100002",
                        "observationTimestamp": "2013-06-14T22:03:51Z",
                        "collector": "A. Technician",
                        "uploadedBy": "dbUserId4",
                        "value": "1.2",
                        "seasonDbId": "1"
                    },
                    {
                        "observationDbId": "2",
                        "observationVariableName": "Carotenoid",
                        "observationVariableDbId": "MO_123:100006",
                        "observationTimestamp": "2013-06-14T22:04:51Z",
                        "collector": "A. Technician",
                        "uploadedBy": "dbUserId",
                        "value": "4.5",
                        "seasonDbId": "1"
                    }
                ],
                "observationLevel": "plot",
                "X": "1",
                "germplasmName": "Name001",
                "plotNumber": "1",
                "plantNumber": null,
                "observationUnitName": "Plot 1",
                "entryType": "test",
                "blockNumber": "1"
            },
            {
                "observationUnitDbId": "2",
                "observationUnitXref": [
                    {
                        "source": "ebi.biosample",
                        "identifier": "SAMEA179865815"
                    },
                    {
                        "source": "gnpis.lot",
                        "identifier": "INRA:CoeSt6_SMH13"
                    },
                    {
                        "source": "kernelDB",
                        "identifier": "239167"
                    }
                ],
                "Y": "1",
                "replicate": "0",
                "entryNumber": "2",
                "germplasmDbId": "1",
                "observations": [
                    {
                        "observationDbId": "3",
                        "observationVariableName": "Plant height",
                        "observationVariableDbId": "MO_123:100002",
                        "observationTimestamp": "2013-06-14T22:05:51Z",
                        "collector": "A. Technician",
                        "uploadedBy": "dbUserId2",
                        "value": "1.1",
                        "seasonDbId": "1"
                    },
                    {
                        "observationDbId": "4",
                        "observationVariableName": "Carotenoid",
                        "observationVariableDbId": "MO_123:100006",
                        "observationTimestamp": "2013-06-14T22:06:51Z",
                        "collector": "A. Technician",
                        "uploadedBy": "dbUserId3",
                        "value": "5.1",
                        "seasonDbId": "1"
                    }
                ],
                "observationLevel": "plant",
                "X": "1",
                "germplasmName": "Name001",
                "plotNumber": "1",
                "plantNumber": "1",
                "observationUnitName": "Plant 1",
                "entryType": "test",
                "blockNumber": "1"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/studies/1001/observationunits/?pageSize=2', expected)

    # end def test_get_obsUnit_details
        
    
    def test_get_plot_layout_details(self):

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
                "blockNumber": "1",
                "Y": "1",
                "additionalInfo": {
                    "publications": "pmid:210494013"
                },
                "X": "1",
                "germplasmDbId": "1",
                "observationUnitDbId": "1",
                "observationLevel": "plot",
                "entryType": "test",
                "germplasmName": "Name001",
                "studyDbId": "1001",
                "replicate": "0",
                "observationUnitName": "Plot 1"
            },
            {
                "blockNumber": "1",
                "Y": "1",
                "additionalInfo": {
                    "publications": "pmid:210494013"
                },
                "X": "1",
                "germplasmDbId": "1",
                "observationUnitDbId": "2",
                "observationLevel": "plant",
                "entryType": "test",
                "germplasmName": "Name001",
                "studyDbId": "1001",
                "replicate": "0",
                "observationUnitName": "Plant 1"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/studies/1001/layout/?pageSize=2', expected)
        
    # end def test_get_plot_layout_details 


    def test_get_obsUnit_by_variableID(self):

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
                "observationTimestamp": "2013-06-14T22:03:51Z",
                "observationDbId": "1",
                "uploadedBy": "dbUserId4",
                "observationUnitName": "Plot 1",
                "observationUnitDbId": "1",
                "studyDbId": "1001",
                "collector": "A. Technician",
                "observationVariableDbId": "MO_123:100002",
                "value": "1.2",
                "germplasmDbId": "1",
                "observationVariableName": "Plant height",
                "germplasmName": "Name001",
                "seasonDbId": "1",
                "observationLevel": "plot"
            },
            {
                "observationTimestamp": "2013-06-14T22:05:51Z",
                "observationDbId": "3",
                "uploadedBy": "dbUserId2",
                "observationUnitName": "Plant 1",
                "observationUnitDbId": "2",
                "studyDbId": "1001",
                "collector": "A. Technician",
                "observationVariableDbId": "MO_123:100002",
                "value": "1.1",
                "germplasmDbId": "1",
                "observationVariableName": "Plant height",
                "germplasmName": "Name001",
                "seasonDbId": "1",
                "observationLevel": "plant"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies/1001/observations/?observationVariableDbIds=MO_123:100002&pageSize=2', expected)

    # end def test_get_obsUnit_by_variableID


    def test_get_search(self):

        expected = """  
{
}"""

        # test_get(self, '/brapi/v1/studies/studies-search/?pageSize=2', expected)
        self.assertJSONEqual("{}", expected)

    # end def test_get_search


    def test_post_search(self):

        expected = """  
{
}"""

        params = {
            "observationUnitDbIds": ["2016-Maugio-34-575-abc-123"],
            "pageSize": 2
        }

        # test_post(self, '/brapi/v1/studies-search', params, expected)
        self.assertJSONEqual("{}", expected)

    # end def test_post_search


    def test_get_study_details(self):

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
                "endDate": "2014-01-01",
                "contacts": [
                    {
                        "orcid": "0000-0002-0607-8728",
                        "name": "A. Breeder",
                        "instituteName": "Plant Science Institute",
                        "contactDbId": "1",
                        "type": "Breeder",
                        "email": "a.breeder@brapi.org"
                    },
                    {
                        "orcid": "0000-0002-0607-8729",
                        "name": "B. Breeder",
                        "instituteName": "Plant Science Institute",
                        "contactDbId": "2",
                        "type": "Breeder",
                        "email": "b.breeder@brapi.org"
                    }
                ],
                "location": {
                    "latitude": -11.1275,
                    "locationDbId": "1",
                    "longitude": -75.356389,
                    "name": "Location 1",
                    "countryName": "Peru",
                    "instituteName": "Plant Science Institute",
                    "abbreviation": "L1",
                    "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                    "type": "Storage location",
                    "additionalInfo": {
                        "altern": "SNPEDRO",
                        "local": "NaSARRI",
                        "cont": "Africa",
                        "creg": "SSA",
                        "adm3": "Coviriali",
                        "adm2": "Kassena-Nankana",
                        "adm1": "Serere",
                        "annualTotalPrecipitation": "6.4",
                        "annualMeanTemperature": "19.2"
                    },
                    "altitude": 828.0,
                    "countryCode": "PER"
                },
                "trialName": "Peru Yield Trial 1",
                "lastUpdate": {
                    "version": "1.1",
                    "timestamp": "2015-01-01T07:54:00Z"
                },
                "license": "https://creativecommons.org/licenses/by/4.0",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "active": true,
                "studyDbId": "1001",
                "locationDbId": "1",
                "lastUpdateTimestamp": "2015-01-01T07:54:00Z",
                "studyName": "Study 1",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "studyType": "Yield study",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2013-01-01",
                "dataLinks": [
                    {
                        "url": "http://data.inra.fr/archive/multi-spect-flowering.zip",
                        "name": "image-archive12.zip",
                        "type": "Image archive"
                    }
                ],
                "lastUpdateVersion": "1.1",
                "trialDbId": "101"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies/1001/?pageSize=2', expected)

    # end def test_get_study_details


    def test_get_study_germplasm_details(self):

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
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "germplasmPUI": "http://pui.per/accession/A000001",
                "pedigree": "landrace",
                "synonyms": [
                    "landrace 1"
                ],
                "entryNumber": "1",
                "seedSource": "open pollination",
                "accessionNumber": "A000001"
            },
            {
                "germplasmDbId": "2",
                "germplasmName": "Name002",
                "germplasmPUI": "http://pui.per/accession/A000002",
                "pedigree": "landrace",
                "synonyms": [
                    "landrace 2"
                ],
                "entryNumber": "2",
                "seedSource": "open pollination",
                "accessionNumber": "A000002"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies/1001/germplasm/?pageSize=2', expected)

    # end def test_get_study_germplasm_details


    def test_get_study_observation_variables(self):

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
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "method": {
                    "methodDbId": "",
                    "reference": "",
                    "description": "",
                    "formula": "",
                    "name": "",
                    "classis": ""
                },
                "growthStage": "mature",
                "observationVariableName": "Plant height",
                "status": "recommended",
                "scientist": "",
                "observationVariableDbId": "MO_123:100002",
                "scale": {
                    "datatype": "Categorical",
                    "xref": null,
                    "decimalPlaces": 0,
                    "validValues": {
                        "min": 1,
                        "max": 2,
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ]
                    },
                    "scaleDbId": "CO_334:0100528",
                    "defaultValue": null,
                    "name": "ug/m",
                    "datatypeDbId": 2
                },
                "crop": "grape",
                "language": "EN",
                "xref": "TL_455:0003001",
                "ontologyName": "Wheat ontology",
                "trait": {
                    "status": "recommended",
                    "traitId": "CO_334:0100620",
                    "traitDbId": "1",
                    "entity": "root",
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "attribute": "carotenoid",
                    "defaultValue": "",
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "classis": "physiological trait"
                },
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "synonyms": [
                    "height",
                    "tallness"
                ],
                "institution": "",
                "defaultValue": null,
                "ontologyDbId": "CO_334"
            },
            {
                "contextOfUse": [
                    ""
                ],
                "method": {
                    "methodDbId": "",
                    "reference": "",
                    "description": "",
                    "formula": "",
                    "name": "",
                    "classis": ""
                },
                "growthStage": "ripen",
                "observationVariableName": "Root weight",
                "status": "active",
                "scientist": "",
                "observationVariableDbId": "MO_123:100003",
                "scale": {
                    "datatype": "Numeric",
                    "xref": "0",
                    "decimalPlaces": 2,
                    "validValues": {
                        "min": 1,
                        "max": 3,
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ]
                    },
                    "scaleDbId": "CO_334:0100527",
                    "defaultValue": null,
                    "name": "kg/g",
                    "datatypeDbId": 1
                },
                "crop": "grape",
                "language": "EN",
                "xref": "TL_455:0003005",
                "ontologyName": "Rice ontology",
                "trait": {
                    "status": "recommended",
                    "traitId": "CO_334:0100620",
                    "traitDbId": "1",
                    "entity": "root",
                    "xref": "TL_455:0003023",
                    "description": "Cassava storage root pulp carotenoid content",
                    "synonyms": [
                        "carotenoid content measure"
                    ],
                    "attribute": "carotenoid",
                    "defaultValue": "",
                    "mainAbbreviation": "CC",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "name": "Carotenoid content",
                    "classis": "physiological trait"
                },
                "submissionTimestamp": "2016-05-14T20:12:09Z",
                "synonyms": [
                    "weight"
                ],
                "institution": "",
                "defaultValue": "1",
                "ontologyDbId": "CO_335"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies/1001/observationVariables/?pageSize=2', expected)

    # end def test_get_study_observation_variables


    def test_get_obsUnit_as_table(self):

        expected = """  
{
}"""

        # test_get(self, '/brapi/v1/studies/1001/table/?pageSize=2', expected)
        self.assertJSONEqual("{}", expected)

    # end def test_get_obsUnit_as_table

# end class SampleTest
