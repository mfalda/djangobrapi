from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class SampleTest(APITestCase):
    
    fixtures = ['crops.json', 'germplasm.json', 'locations.json', 'samples.json']
    

    def test_get_samples(self):

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
                "studyDbId": "StudyId-123",
                "locationDbId": "LocationId-123",
                "plotId": "PlotId-123",
                "plantId": "PlantID-123",
                "sampleId": "Unique-Plant-SampleID",
                "takenBy": "Mr. Technician",
                "sampleTimestamp": "2016-07-27T13:43:22Z",
                "sampleType": "TypeOfSample",
                "tissueType": "TypeOfTissue",
                "notes": "Cut from infected leaf",
                "studyName": "Yield Trial A",
                "season": "Summer",
                "locationName": "Kenya",
                "entryNumber": 11,
                "plotNumber": 1,
                "germplasmDbId": 15,
                "plantingTimestamp": "2016-01-01T22:22:21Z",
                "harvestTimestamp": "2016-06-30T22:33:23Z"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/samples/Unique-Plant-SampleID', expected)
        
    # end def test_get_samples

# end class SampleTest
