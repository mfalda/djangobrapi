from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.samples import SampleView
from brapi.models.sample import Sample


class SampleTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database
        Sample.objects.create(studyDbId='StudyId-123', locationDbId='LocationId-123', plotId='PlotId-123', 
            plantId='PlantID-123', sampleId='Unique-Plant-SampleID', takenBy='Mr. Technician', 
            sampleTimestamp='2016-07-27T14:43:22+0100', sampleType='TypeOfSample', tissueType='TypeOfTissue', 
            notes='Cut from infected leaf', studyName='Yield Trial A', season='Summer', locationName='Kenya', 
            entryNumber=11, plotNumber=1, germplasmDbId=15, plantingTimestamp='2016-01-01T23:22:21+0100', 
            harvestTimestamp='2016-06-30T23:33:23+0100')

    # end def setUP


    def test_get_samples(self):

        view = SampleView.as_view()

        factory = APIRequestFactory()
        request = factory.get('/brapi/b1/samples/Unique-Plant-SampleID')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content` without this.
        self.assertJSONEqual(response.content.decode('utf-8'), """
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
}""")

    # end def test_get_samples

# end class SampleTest
