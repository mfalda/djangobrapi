from rest_framework.test import APITestCase

from brapi.aux_fun import test_post


class PhenotypeTest(APITestCase):
    
    fixtures = ['crops.json', 'valid_values.json', 'ontologies.json',
                'methods.json', 'scales.json', 'seasons.json',
                'traits.json', 'observation_variables.json', 'treatments.json',
                'germplasm.json', 'programs.json', 'trials.json',
                'locations.json', 'contacts.json', 'location_addInfo.json',
                'study_types.json', 'studies.json', 'datatypes.json',
                'observation_units.json', 'observation_unit_xrefs', 'observations.json']
    
    
    def test_post_phenotypes_search(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 6,
            "totalCount": 11,
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
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "observationUnitName": "Plot 1",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
            },
            {
                "observationUnitDbId": "10",
                "observationUnitXref": [],
                "observations": [
                    {
                        "observationDbId": "16",
                        "observationVariableName": "Plant height",
                        "observationVariableDbId": "MO_123:100002",
                        "observationTimestamp": "2011-06-14T22:06:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId1",
                        "value": "100",
                        "seasonDbId": "2"
                    },
                    {
                        "observationDbId": "17",
                        "observationVariableName": "Root weight",
                        "observationVariableDbId": "MO_123:100003",
                        "observationTimestamp": "2011-06-14T22:07:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId",
                        "value": "9",
                        "seasonDbId": "2"
                    },
                    {
                        "observationDbId": "18",
                        "observationVariableName": "Virus susceptibility",
                        "observationVariableDbId": "MO_123:100005",
                        "observationTimestamp": "2011-06-14T22:08:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId",
                        "value": "2",
                        "seasonDbId": "2"
                    }
                ],
                "treatments": [],
                "observationUnitName": "Plant 5",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1003",
                "studyName": "Study 3",
                "locationDbId": "2",
                "locationName": "Location 2",
                "observationLevel": "plant",
                "observationLevels": "block:101;plot:5;plant:5",
                "plotNumber": "5",
                "plantNumber": "5",
                "blockNumber": "101",
                "replicate": "1",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "4",
                "germplasmName": "Name004",
                "X": "1",
                "Y": "1"
            }
        ]
    }
}"""

        params = {}

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_phenotypes_search


    def test_post_phenotypes_search_germplasm(self):

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
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "observationUnitName": "Plot 1",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
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
                "treatments": [],
                "observationUnitName": "Plant 1",
                "entryNumber": "2",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plant",
                "observationLevels": "block:1;plot:1;plant:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Improvement Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
            }
        ]
    }
}"""
        
        params = {
            "germplasmDbIds": [1]
        }

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_phenotypes_search_germplasm


    def test_post_phenotypes_search_observationVariables(self):

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
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "observationUnitName": "Plot 1",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
            }
        ]
    }
}"""

        params = {
            "observationVariableDbIds": ["MO_123:100002"]
        }

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_phenotypes_search_observationVariables


    def test_post_phenotypes_search_studies(self):

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
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "observationUnitName": "Plot 1",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
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
                "treatments": [],
                "observationUnitName": "Plant 1",
                "entryNumber": "2",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plant",
                "observationLevels": "block:1;plot:1;plant:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Improvement Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
            }
        ]
    }
}"""

        params = {
            "studyDbIds": ["1001"]
        }

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_phenotypes_search_studies


    def test_post_phenotypes_search_locations(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 4,
            "totalCount": 8,
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
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "observationUnitName": "Plot 1",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
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
                "treatments": [],
                "observationUnitName": "Plant 1",
                "entryNumber": "2",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plant",
                "observationLevels": "block:1;plot:1;plant:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Improvement Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
            }
        ]
    }
}"""

        params = {
            "locationDbIds": ["1"]
        }

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_phenotypes_search_locations
        

    def test_post_phenotypes_search_programs(self):

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
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "observationUnitName": "Plot 1",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
            },
            {
                "observationUnitDbId": "10",
                "observationUnitXref": [],
                "observations": [
                    {
                        "observationDbId": "16",
                        "observationVariableName": "Plant height",
                        "observationVariableDbId": "MO_123:100002",
                        "observationTimestamp": "2011-06-14T22:06:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId1",
                        "value": "100",
                        "seasonDbId": "2"
                    },
                    {
                        "observationDbId": "17",
                        "observationVariableName": "Root weight",
                        "observationVariableDbId": "MO_123:100003",
                        "observationTimestamp": "2011-06-14T22:07:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId",
                        "value": "9",
                        "seasonDbId": "2"
                    },
                    {
                        "observationDbId": "18",
                        "observationVariableName": "Virus susceptibility",
                        "observationVariableDbId": "MO_123:100005",
                        "observationTimestamp": "2011-06-14T22:08:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId",
                        "value": "2",
                        "seasonDbId": "2"
                    }
                ],
                "treatments": [],
                "observationUnitName": "Plant 5",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1003",
                "studyName": "Study 3",
                "locationDbId": "2",
                "locationName": "Location 2",
                "observationLevel": "plant",
                "observationLevels": "block:101;plot:5;plant:5",
                "plotNumber": "5",
                "plantNumber": "5",
                "blockNumber": "101",
                "replicate": "1",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "4",
                "germplasmName": "Name004",
                "X": "1",
                "Y": "1"
            }
        ]
    }
}"""

        params = {
            "programDbIds": [1]
        }

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_phenotypes_search_programs


    def test_post_phenotypes_search_seasons(self):

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
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "observationUnitName": "Plot 1",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
            }
        ]
    }
}"""

        params = {
            "seasonDbIds": [1]
        }

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_phenotypes_search_seasons


    def test_post_phenotypes_search_observationLevels(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 6,
            "totalCount": 11,
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
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "observationUnitName": "Plot 1",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
            },
            {
                "observationUnitDbId": "10",
                "observationUnitXref": [],
                "observations": [
                    {
                        "observationDbId": "16",
                        "observationVariableName": "Plant height",
                        "observationVariableDbId": "MO_123:100002",
                        "observationTimestamp": "2011-06-14T22:06:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId1",
                        "value": "100",
                        "seasonDbId": "2"
                    },
                    {
                        "observationDbId": "17",
                        "observationVariableName": "Root weight",
                        "observationVariableDbId": "MO_123:100003",
                        "observationTimestamp": "2011-06-14T22:07:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId",
                        "value": "9",
                        "seasonDbId": "2"
                    },
                    {
                        "observationDbId": "18",
                        "observationVariableName": "Virus susceptibility",
                        "observationVariableDbId": "MO_123:100005",
                        "observationTimestamp": "2011-06-14T22:08:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId",
                        "value": "2",
                        "seasonDbId": "2"
                    }
                ],
                "treatments": [],
                "observationUnitName": "Plant 5",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1003",
                "studyName": "Study 3",
                "locationDbId": "2",
                "locationName": "Location 2",
                "observationLevel": "plant",
                "observationLevels": "block:101;plot:5;plant:5",
                "plotNumber": "5",
                "plantNumber": "5",
                "blockNumber": "101",
                "replicate": "1",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "4",
                "germplasmName": "Name004",
                "X": "1",
                "Y": "1"
            }
        ]
    }
}"""

        params = {
            "observationLevel": ["plot"]
        }

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_phenotypes_search_observationLevels


    def test_post_phenotypes_search_observationTimeStampRange(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 6,
            "totalCount": 11,
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
                "treatments": [
                    {
                        "factor": "water regimen",
                        "modality": "water deficit"
                    }
                ],
                "observationUnitName": "Plot 1",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1001",
                "studyName": "Study 1",
                "locationDbId": "1",
                "locationName": "Location 1",
                "observationLevel": "plot",
                "observationLevels": "block:1;plot:1",
                "plotNumber": "1",
                "plantNumber": "1",
                "blockNumber": "1",
                "replicate": "0",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "1",
                "germplasmName": "Name001",
                "X": "1",
                "Y": "1"
            },
            {
                "observationUnitDbId": "10",
                "observationUnitXref": [],
                "observations": [
                    {
                        "observationDbId": "16",
                        "observationVariableName": "Plant height",
                        "observationVariableDbId": "MO_123:100002",
                        "observationTimestamp": "2011-06-14T22:06:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId1",
                        "value": "100",
                        "seasonDbId": "2"
                    },
                    {
                        "observationDbId": "17",
                        "observationVariableName": "Root weight",
                        "observationVariableDbId": "MO_123:100003",
                        "observationTimestamp": "2011-06-14T22:07:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId",
                        "value": "9",
                        "seasonDbId": "2"
                    },
                    {
                        "observationDbId": "18",
                        "observationVariableName": "Virus susceptibility",
                        "observationVariableDbId": "MO_123:100005",
                        "observationTimestamp": "2011-06-14T22:08:51Z",
                        "collector": "B. Tech",
                        "uploadedBy": "dbUserId",
                        "value": "2",
                        "seasonDbId": "2"
                    }
                ],
                "treatments": [],
                "observationUnitName": "Plant 5",
                "entryNumber": "1",
                "entryType": "test",
                "studyDbId": "1003",
                "studyName": "Study 3",
                "locationDbId": "2",
                "locationName": "Location 2",
                "observationLevel": "plant",
                "observationLevels": "block:101;plot:5;plant:5",
                "plotNumber": "5",
                "plantNumber": "5",
                "blockNumber": "101",
                "replicate": "1",
                "programName": "Wheat Resistance Program",
                "germplasmDbId": "4",
                "germplasmName": "Name004",
                "X": "1",
                "Y": "1"
            }
        ]
    }
}"""

        params = {
            "observationTimeStampRange": ["2011-05-14T22:06:51Z", "2013-07-14T22:04:51Z"]
        }

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_phenotypes_search_observationTimeStampRange

# end class PhenotypeTest
