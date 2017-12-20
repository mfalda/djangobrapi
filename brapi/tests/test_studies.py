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


    def test_get_seasons_year(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "season": "Spring",
                "year": "2013",
                "seasonDbId": "1"
            },
            {
                "season": "Winter",
                "year": "2013",
                "seasonDbId": "4"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/seasons/?year=2013&pageSize=2', expected)

    # end def test_get_seasons_year


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
                "plantNumber": "1",
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


    def test_get_obsUnit_details_obsLevel(self):

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
                "replicate": "0",
                "plotNumber": "1",
                "observationUnitName": "Plot 1",
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
                "observationUnitDbId": "1",
                "germplasmDbId": "1",
                "entryType": "test",
                "entryNumber": "1",
                "germplasmName": "Name001",
                "X": "1",
                "plantNumber": "1",
                "blockNumber": "1",
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
                "Y": "1"
            },
            {
                "replicate": "0",
                "plotNumber": "2",
                "observationUnitName": "Plot 2",
                "observationUnitXref": [
                    {
                        "source": "ebi.biosample",
                        "identifier": "SAMEA179865682"
                    },
                    {
                        "source": "gnpis.lot",
                        "identifier": "INRA:CoeSt6_SMH51"
                    },
                    {
                        "source": "kernelDB",
                        "identifier": "239146"
                    }
                ],
                "observationUnitDbId": "3",
                "germplasmDbId": "2",
                "entryType": "test",
                "entryNumber": "3",
                "germplasmName": "Name002",
                "X": "1",
                "plantNumber": null,
                "blockNumber": "1",
                "observations": [
                    {
                        "observationDbId": "5",
                        "observationVariableName": "Root weight",
                        "observationVariableDbId": "MO_123:100003",
                        "observationTimestamp": "2013-06-14T22:07:51Z",
                        "collector": "A. Technician",
                        "uploadedBy": "dbUserId3",
                        "value": "2.1",
                        "seasonDbId": "4"
                    },
                    {
                        "observationDbId": "6",
                        "observationVariableName": "Root color",
                        "observationVariableDbId": "MO_123:100004",
                        "observationTimestamp": "2013-06-14T22:08:51Z",
                        "collector": "A. Technician",
                        "uploadedBy": "dbUserId4",
                        "value": "dark blue",
                        "seasonDbId": "4"
                    }
                ],
                "observationLevel": "plot",
                "Y": "2"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/studies/1001/observationunits/?observationLevel=plot&pageSize=2', expected)

    # end def test_get_obsUnit_details_obsLevel


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
                "growthStage": "mature",
                "contextOfUse": [
                    "Trial evaluation",
                    "Nursery evaluation"
                ],
                "institution": "",
                "trait": {
                    "traitDbId": "1",
                    "entity": "root",
                    "attribute": "carotenoid",
                    "status": "recommended",
                    "traitId": "CO_334:0100620",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "classis": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "defaultValue": "",
                    "synonyms": [
                        "carotenoid content measure"
                    ]
                },
                "crop": "grape",
                "observationVariableName": "Plant height",
                "scale": {
                    "validValues": {
                        "categories": [
                            "1=cold",
                            "2=hot"
                        ],
                        "max": 2,
                        "min": 1
                    },
                    "scaleDbId": "CO_334:0100528",
                    "xref": null,
                    "decimalPlaces": 0,
                    "datatype": "Categorical",
                    "name": "ug/m",
                    "defaultValue": null,
                    "datatypeDbId": 2
                },
                "status": "recommended",
                "scientist": "",
                "xref": "TL_455:0003001",
                "language": "EN",
                "submissionTimestamp": "2016-05-17T20:22:09Z",
                "datatype": "Categorical",
                "observationVariableDbId": "MO_123:100002",
                "defaultValue": null,
                "method": {
                    "methodDbId": "CO_334:0010320",
                    "classis": "Estimation",
                    "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart",
                    "name": "Visual Rating:total carotenoid by chart_method",
                    "reference": null,
                    "formula": null
                },
                "ontologyDbId": "CO_334",
                "ontologyName": "Wheat ontology",
                "synonyms": [
                    "height",
                    "tallness"
                ]
            },
            {
                "growthStage": "ripen",
                "contextOfUse": [
                    ""
                ],
                "institution": "",
                "trait": {
                    "traitDbId": "1",
                    "entity": "root",
                    "attribute": "carotenoid",
                    "status": "recommended",
                    "traitId": "CO_334:0100620",
                    "alternativeAbbreviations": [
                        "CCS"
                    ],
                    "xref": "TL_455:0003023",
                    "classis": "physiological trait",
                    "description": "Cassava storage root pulp carotenoid content",
                    "name": "Carotenoid content",
                    "mainAbbreviation": "CC",
                    "defaultValue": "",
                    "synonyms": [
                        "carotenoid content measure"
                    ]
                },
                "crop": "grape",
                "observationVariableName": "Root weight",
                "scale": {
                    "validValues": {
                        "categories": [
                            "1=low",
                            "2=medium",
                            "3=high"
                        ],
                        "max": 3,
                        "min": 1
                    },
                    "scaleDbId": "CO_334:0100527",
                    "xref": "0",
                    "decimalPlaces": 2,
                    "datatype": "Numeric",
                    "name": "kg/g",
                    "defaultValue": null,
                    "datatypeDbId": 1
                },
                "status": "active",
                "scientist": "",
                "xref": "TL_455:0003005",
                "language": "EN",
                "submissionTimestamp": "2016-05-14T20:12:09Z",
                "datatype": "Numeric",
                "observationVariableDbId": "MO_123:100003",
                "defaultValue": "1",
                "method": null,
                "ontologyDbId": "CO_335",
                "ontologyName": "Rice ontology",
                "synonyms": [
                    "weight"
                ]
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


class StudySearchTest(APITestCase):

    fixtures = ['crops.json', 'programs.json', 'trials.json', 'locations.json', 'contacts.json',
                'location_addInfo.json', 'study_types.json', 'studies.json', 'seasons.json',
                'study_observation_levels.json', 'study_seasons.json', 'datalinks.json', 'datatypes.json',
                'study_contacts.json', 'study_types.json', 'study_addInfo.json', 'valid_values.json', 'traits.json',
                'germplasm.json', 'observation_units.json', 'observation_units_addInfo.json',
                'methods.json', 'scales.json', 'ontologies.json', 'observations.json', 'observation_variables.json',
                'observation_unit_xrefs.json']


    def test_get_study_search(self):

        expected = """  
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "studyType": "Yield study",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "studyName": "Study 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2013-01-01",
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "endDate": "2014-01-01",
                "active": true,
                "studyDbId": "1001"
            },
            {
                "seasons": [
                    "2014 Spring"
                ],
                "studyType": "Yield study",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "studyName": "Study 2",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2014-01-01",
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "endDate": "2015-01-01",
                "active": true,
                "studyDbId": "1002"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?pageSize=2', expected)

    # end def test_get_study_search


    def test_get_study_search_type(self):

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
                "startDate": "2013-01-01",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationName": "Location 1",
                "studyType": "Yield study",
                "trialName": "Peru Yield Trial 1",
                "active": true,
                "endDate": "2014-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",                
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationDbId": "1",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDescription": "Field yield phenotyping study"
            },
            {
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "studyName": "Study 2",
                "locationName": "Location 1",
                "studyType": "Yield study",
                "trialName": "Peru Yield Trial 1",
                "active": true,
                "endDate": "2015-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationDbId": "1",
                "seasons": [
                    "2014 Spring"
                ],
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDescription": "Field yield phenotyping study"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?studyType=Yield study&pageSize=2', expected)

    # end def test_get_study_search_type


    def test_get_study_search_season(self):

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
                "studyType": "Yield study",
                "studyName": "Study 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationName": "Location 1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "active": true,
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "endDate": "2014-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",                
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "studyDbId": "1001"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?seasonDbId=1&pageSize=2', expected)

    # end def test_get_study_search_season


    def test_get_study_search_location(self):

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
                "studyType": "Yield study",
                "studyName": "Study 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationName": "Location 1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "active": true,
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "endDate": "2014-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",                
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "studyDbId": "1001"
            },
            {
                "studyType": "Yield study",
                "studyName": "Study 2",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationName": "Location 1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "active": true,
                "startDate": "2014-01-01",
                "seasons": [
                    "2014 Spring"
                ],
                "endDate": "2015-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "studyDbId": "1002"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?locationDbId=1&pageSize=2', expected)

    # end def test_get_study_search_location


    def test_get_study_search_program(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "studyType": "Yield study",
                "studyName": "Study 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationName": "Location 1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "active": true,
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "endDate": "2014-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "studyDbId": "1001"
            },
            {
                "studyType": "Yield study",
                "studyName": "Study 2",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationName": "Location 1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "active": true,
                "startDate": "2014-01-01",
                "seasons": [
                    "2014 Spring"
                ],
                "endDate": "2015-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "studyDbId": "1002"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?programDbId=1&pageSize=2', expected)

    # end def test_get_study_search_program


    def test_get_study_search_germplasm(self):

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
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "studyType": "Yield study",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "studyName": "Study 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2013-01-01",
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "endDate": "2014-01-01",
                "active": true,
                "studyDbId": "1001"
            },
            {
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "studyType": "Yield study",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "studyName": "Study 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2013-01-01",
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "endDate": "2014-01-01",
                "active": true,
                "studyDbId": "1001"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?germplasmDbIds=1&pageSize=2', expected)

    # end def test_get_study_search_germplasm


    def test_get_study_search_observationVariable(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 3,
            "totalCount": 6,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1001",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2014-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 1"
            },
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1001",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2014-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 1"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?observationVariableDbIds=MO_123:100002&pageSize=2', expected)

    # end def test_get_study_search_observationVariable


    def test_get_study_search_active(self):

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
                "studyType": "Yield study",
                "studyName": "Study 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationName": "Location 1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "active": true,
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "endDate": "2014-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "studyDbId": "1001"
            },
            {
                "studyType": "Yield study",
                "studyName": "Study 2",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationName": "Location 1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "active": true,
                "startDate": "2014-01-01",
                "seasons": [
                    "2014 Spring"
                ],
                "endDate": "2015-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "studyDbId": "1002"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?active=true&pageSize=2', expected)

    # end def test_get_study_search_active


    def test_get_study_search_NOTactive(self):

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
                "seasons": [],
                "endDate": "2012-01-01",
                "startDate": "2011-01-01",
                "trialDbId": "102",
                "locationName": "Location 2",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",                
                "studyDbId": "1003",
                "studyName": "Study 3",
                "studyType": "Crossing Nursery",
                "active": false,
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDescription": "Nursery study studyDescription",
                "locationDbId": "2",
                "trialName": "Peru Yield Trial 2",
                "license": "https://creativecommons.org/licenses/by/4.0"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?active=false&pageSize=2', expected)

    # end def test_get_study_search_NOTactive


    def test_get_study_search_sortedAsc(self):

        expected = """  
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "endDate": "2014-01-01",
                "startDate": "2013-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "locationName": "Location 1",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "studyType": "Yield study",
                "active": true,
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "license": "https://creativecommons.org/licenses/by/4.0"
            },
            {
                "seasons": [
                    "2014 Spring"
                ],
                "endDate": "2015-01-01",
                "startDate": "2014-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "locationName": "Location 1",
                "studyDbId": "1002",
                "studyName": "Study 2",
                "studyType": "Yield study",
                "active": true,
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "license": "https://creativecommons.org/licenses/by/4.0"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?sortBy=studyName&sortOrder=asc&pageSize=2', expected)

    # end def test_get_study_search_sortedAsc


    def test_get_study_search_sortedDesc(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "seasons": [],
                "studyType": "Crossing Nursery",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 2",
                "studyName": "Study 3",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Nursery study studyDescription",
                "startDate": "2011-01-01",
                "trialName": "Peru Yield Trial 2",
                "trialDbId": "102",
                "locationDbId": "2",
                "programName": "Wheat Resistance Program",
                "endDate": "2012-01-01",
                "active": false,
                "studyDbId": "1003"
            },
            {
                "seasons": [
                    "2014 Spring"
                ],
                "studyType": "Yield study",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "studyName": "Study 2",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2014-01-01",
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "endDate": "2015-01-01",
                "active": true,
                "studyDbId": "1002"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies-search/?sortBy=studyName&sortOrder=desc&pageSize=2', expected)

    # end def test_get_study_search_sortedDesc


    def test_post_study_search(self):

        expected = """  
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1001",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2014-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 1"
            },
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2014-01-01",
                "seasons": [
                    "2014 Spring"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1002",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2015-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 2"
            }
        ]
    }
}"""

        params = {}

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search


    def test_post_study_search_type(self):

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
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "endDate": "2014-01-01",
                "startDate": "2013-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "locationName": "Location 1",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "studyType": "Yield study",
                "active": true,
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "license": "https://creativecommons.org/licenses/by/4.0"
            },
            {
                "seasons": [
                    "2014 Spring"
                ],
                "endDate": "2015-01-01",
                "startDate": "2014-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "locationName": "Location 1",
                "studyDbId": "1002",
                "studyName": "Study 2",
                "studyType": "Yield study",
                "active": true,
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "license": "https://creativecommons.org/licenses/by/4.0"
            }
        ]
    }
}"""

        params = {
            "studyType": ["Yield study"]
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_type


    def test_post_study_search_names(self):

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
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "endDate": "2014-01-01",
                "startDate": "2013-01-01",
                "trialDbId": "101",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",
                "locationName": "Location 1",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "studyType": "Yield study",
                "active": true,
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "trialName": "Peru Yield Trial 1",
                "license": "https://creativecommons.org/licenses/by/4.0"
            },
            {
                "seasons": [],
                "endDate": "2012-01-01",
                "startDate": "2011-01-01",
                "trialDbId": "102",
                "locationName": "Location 2",
                "programDbId": "1", 
                "programName": "Wheat Resistance Program",                            
                "studyDbId": "1003",
                "studyName": "Study 3",
                "studyType": "Crossing Nursery",
                "active": false,
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDescription": "Nursery study studyDescription",
                "locationDbId": "2",
                "trialName": "Peru Yield Trial 2",
                "license": "https://creativecommons.org/licenses/by/4.0"
            }
        ]
    }
}"""

        params = {
            "studyNames": ["Study 1", "Study 3"]
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_names


    def test_post_study_search_locations(self):

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
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "studyType": "Yield study",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "studyName": "Study 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2013-01-01",
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "endDate": "2014-01-01",
                "active": true,
                "studyDbId": "1001"
            },
            {
                "seasons": [
                    "2014 Spring"
                ],
                "studyType": "Yield study",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "studyName": "Study 2",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2014-01-01",
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "endDate": "2015-01-01",
                "active": true,
                "studyDbId": "1002"
            }
        ]
    }
}"""

        params = {
            "studyLocations": ["Location 1"]
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_locations


    def test_post_study_search_programs(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "programDbId": "1",                
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "startDate": "2013-01-01",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "endDate": "2014-01-01",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyType": "Yield study",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "studyDescription": "Field yield phenotyping study",
                "trialName": "Peru Yield Trial 1",
                "active": true
            },
            {
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "seasons": [
                    "2014 Spring"
                ],
                "startDate": "2014-01-01",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "endDate": "2015-01-01",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyType": "Yield study",
                "studyDbId": "1002",
                "studyName": "Study 2",
                "studyDescription": "Field yield phenotyping study",
                "trialName": "Peru Yield Trial 1",
                "programDbId": "1",
                "active": true
            }
        ]
    }
}"""

        params = {
            "programNames": ["Wheat Resistance Program"]
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_programs


    def test_post_study_search_germplasm(self):

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
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "studyType": "Yield study",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "studyName": "Study 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2013-01-01",
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "endDate": "2014-01-01",
                "active": true,
                "studyDbId": "1001"
            },
            {
                "seasons": [
                    "2014 Spring"
                ],
                "studyType": "Yield study",
                "programDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "locationName": "Location 1",
                "studyName": "Study 2",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2014-01-01",
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "locationDbId": "1",
                "programName": "Wheat Resistance Program",
                "endDate": "2015-01-01",
                "active": true,
                "studyDbId": "1002"
            }
        ]
    }
}"""

        params = {
            "germplasmDbIds": [1]
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_germplasm


    def test_post_study_search_observationVariables(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1001",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2014-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 1"
            },
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2014-01-01",
                "seasons": [
                    "2014 Spring"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1002",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2015-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 2"
            }
        ]
    }
}"""

        params = {
            "observationVariableDbIds": ["MO_123:100002"]
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_observationVariables


    def test_post_study_search_trials(self):

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
                "trialName": "Peru Yield Trial 1",
                "startDate": "2013-01-01",
                "locationName": "Location 1",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "trialDbId": "101",
                "locationDbId": "1",
                "programDbId": "1",                
                "programName": "Wheat Resistance Program",
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDbId": "1001",
                "endDate": "2014-01-01",
                "studyName": "Study 1",
                "studyType": "Yield study",
                "active": true,
                "license": "https://creativecommons.org/licenses/by/4.0"
            },
            {
                "trialName": "Peru Yield Trial 1",
                "startDate": "2014-01-01",
                "locationName": "Location 1",
                "seasons": [
                    "2014 Spring"
                ],
                "trialDbId": "101",
                "locationDbId": "1",
                "programDbId": "1",               
                "programName": "Wheat Resistance Program",                
                "studyDescription": "Field yield phenotyping study",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyDbId": "1002",
                "endDate": "2015-01-01",
                "studyName": "Study 2",
                "studyType": "Yield study",
                "active": true,
                "license": "https://creativecommons.org/licenses/by/4.0"
            }
        ]
    }
}"""

        params = {
            "trialDbIds": ["101"]
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_trials


    def test_post_study_search_active(self):

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
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1001",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2014-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 1"
            },
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2014-01-01",
                "seasons": [
                    "2014 Spring"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1002",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2015-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 2"
            }
        ]
    }
}"""

        params = {
            "active": "true"
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_active


    def test_post_study_search_NOTactive(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1001",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2014-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 1"
            },
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2014-01-01",
                "seasons": [
                    "2014 Spring"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1002",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2015-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 2"
            }
        ]
    }
}"""

        params = {
            "active": "false"
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_NOTactive


    def test_post_study_search_sortedAsc(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2013-01-01",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1001",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2014-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 1"
            },
            {
                "locationName": "Location 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "studyDescription": "Field yield phenotyping study",
                "programName": "Wheat Resistance Program",
                "startDate": "2014-01-01",
                "seasons": [
                    "2014 Spring"
                ],
                "trialName": "Peru Yield Trial 1",
                "trialDbId": "101",
                "studyDbId": "1002",
                "locationDbId": "1",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyType": "Yield study",
                "endDate": "2015-01-01",
                "active": true,
                "programDbId": "1",
                "studyName": "Study 2"
            }
        ]
    }
}"""

        params = {
            "sortBy": "studyName",
            "sortOrder": "asc"
        }

        test_post(self, '/brapi/v1/studies-search?&pageSize=2', params, expected)

    # end def test_post_study_search_sortedAsc


    def test_post_study_search_sortedDesc(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "locationName": "Location 2",
                "trialDbId": "102",
                "seasons": [],
                "studyDescription": "Nursery study studyDescription",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyName": "Study 3",
                "startDate": "2011-01-01",
                "studyDbId": "1003",
                "trialName": "Peru Yield Trial 2",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationDbId": "2",
                "endDate": "2012-01-01",
                "programDbId": "1",
                "studyType": "Crossing Nursery",
                "active": false,
                "programName": "Wheat Resistance Program"
            },
            {
                "locationName": "Location 1",
                "trialDbId": "101",
                "seasons": [
                    "2014 Spring"
                ],
                "studyDescription": "Field yield phenotyping study",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "studyName": "Study 2",
                "startDate": "2014-01-01",
                "studyDbId": "1002",
                "trialName": "Peru Yield Trial 1",
                "license": "https://creativecommons.org/licenses/by/4.0",
                "locationDbId": "1",
                "endDate": "2015-01-01",
                "programDbId": "1",
                "studyType": "Yield study",
                "active": true,
                "programName": "Wheat Resistance Program"
            }
        ]
    }
}"""

        params = {
            "sortBy": "studyName",
            "sortOrder": "desc"
        }

        test_post(self, '/brapi/v1/studies-search?pageSize=2', params, expected)

    # end def test_post_study_search_sortedDesc
        
# end class StudySearchTest
