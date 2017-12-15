from rest_framework.test import APITestCase

from brapi.aux_fun import test_post


class PhenotypeTest(APITestCase):
    
    fixtures = ['crops.json', 'valid_values.json', 'ontologies.json',
                'methods.json', 'scales.json', 'seasons.json',
                'traits.json', 'observation_variables.json',
                'germplasm.json', 'programs.json', 'trials.json',
                'locations.json', 'contacts.json', 'location_addInfo.json',
                'study_types.json', 'studies.json', 'datatypes.json',
                'observation_units.json', 'observations.json']
    
    
    def test_post_search(self):

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
                "observationUnitDbId": "1",
                "observationUnitXref": [
                    {
                        "source": "ebi.biosample",
                        "identifier": "SAMEA179865230"
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
                "Y": "1",
                "observationVariableDbId": "MO_123:100002",
                "season": "Spring",
                "observationDbId": "1",
                "observationTimestamp": "2013-06-14T22:03:51Z"
            },
            {
                "observationUnitDbId": "1",
                "observationUnitXref": [
                    {
                        "source": "ebi.biosample",
                        "identifier": "SAMEA179865230"
                    }
                ],
                "observations": [
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
                "Y": "1",
                "observationVariableDbId": "MO_123:100006",
                "season": "Spring",
                "observationDbId": "2",
                "observationTimestamp": "2013-06-14T22:04:51Z"
            }
        ]
    }
}"""
        params = {
            "observationUnitDbIds": ["2016-Maugio-34-575-abc-123"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/phenotypes-search/?pageSize=2', params, expected)

    # end def test_post_search

# end class PhenotypeTest
