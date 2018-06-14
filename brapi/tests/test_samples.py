from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class SampleTest(APITestCase):
    
    fixtures = ['crops.json', 'germplasm.json', 'locations.json',
                'observation_units.json', 'seasons.json', 'programs.json',
                'trials.json', 'locations.json', 'study_types.json', 'studies.json',
                'samples.json']
    

    def test_get_samples(self):

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
                "notes": "Cut from infected leaf",
                "plantingTimestamp": "2016-01-01T22:22:21Z",
                "germplasmDbId": "1",
                "sampleDbId": "1",
                "plantId": "PlantID-123",
                "sampleType": "TypeOfSample",
                "sampleTimestamp": "2016-07-27T13:43:22Z",
                "season": "Spring",
                "entryNumber": "1",
                "studyDbId": "1001",
                "observationUnitDbId": "1",
                "plotNumber": "1",
                "locationName": "Location 1",
                "plotId": "PlotId-123",
                "takenBy": "Mr. Technician",
                "sampleId": "Unique-Plant-SampleID",
                "harvestTimestamp": "2016-06-30T22:33:23Z",
                "tissueType": "TypeOfTissue",
                "locationDbId": "1"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/samples/Unique-Plant-SampleID/', expected)
        
    # end def test_get_samples


    def test_get_search_samples(self):

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
                "notes": "Cut from infected leaf",
                "plantingTimestamp": "2016-01-01T22:22:21Z",
                "germplasmDbId": "1",
                "sampleDbId": "1",
                "plantId": "PlantID-123",
                "sampleType": "TypeOfSample",
                "sampleTimestamp": "2016-07-27T13:43:22Z",
                "season": "Spring",
                "entryNumber": "1",
                "studyDbId": "1001",
                "observationUnitDbId": "1",
                "plotNumber": "1",
                "locationName": "Location 1",
                "plotId": "PlotId-123",
                "takenBy": "Mr. Technician",
                "sampleId": "Unique-Plant-SampleID",
                "harvestTimestamp": "2016-06-30T22:33:23Z",
                "tissueType": "TypeOfTissue",
                "locationDbId": "1"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/samples-search/?sampleDbId=Unique-Plant-SampleID', expected)

    # end def test_get_search_samples


    def test_post_search_samples(self):

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
                "notes": "Cut from infected leaf",
                "plantingTimestamp": "2016-01-01T22:22:21Z",
                "germplasmDbId": "1",
                "sampleDbId": "1",
                "plantId": "PlantID-123",
                "sampleType": "TypeOfSample",
                "sampleTimestamp": "2016-07-27T13:43:22Z",
                "season": "Spring",
                "entryNumber": "1",
                "studyDbId": "1001",
                "observationUnitDbId": "1",
                "plotNumber": "1",
                "locationName": "Location 1",
                "plotId": "PlotId-123",
                "takenBy": "Mr. Technician",
                "sampleId": "Unique-Plant-SampleID",
                "harvestTimestamp": "2016-06-30T22:33:23Z",
                "tissueType": "TypeOfTissue",
                "locationDbId": "1"
            }
        ]
    }
}"""

        params = {
            "sampleDbId": ["Unique-Plant-SampleID"]
        }

        test_get(self, '/brapi/v1/samples-search', expected)

    # end def test_post_search_samples

# end class SampleTest

