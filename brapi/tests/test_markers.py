from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.markers import MarkerViewSet
from brapi.models.marker import Marker


class MarkerTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database
        Marker.objects.create(markerDbId='1', defaultDisplayName='a_01_10001', 
                              type='SNP', synonyms=['i_01_10001', 'popA_10001'], 
                              refAlt=['A', 'T'], analysisMethods=['illumina'])
        Marker.objects.create(markerDbId='2', defaultDisplayName='A_01_10002', 
                              type='SNP', synonyms=['i_01_10001', 'popA_10002'], 
                              refAlt=['G', 'C'], analysisMethods=['illumina'])

    # end def setUP


    def test_get_markers(self):

        view = MarkerViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/v1/markers/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content.decode('utf-8')` without this.
        self.assertJSONEqual(response.content.decode('utf-8'), """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 2,
            "pageSize": 100
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
{
                "markerDbId": 1,
                "defaultDisplayName": "a_01_10001",
                "type": "SNP",
                "synonyms": [
                    "i_01_10001",
                    "popA_10001"
                ],
                "refAlt": [
                    "A",
                    "T"
                ],
                "analysisMethods": [
                    "illumina"
                ]
            },
            {
                "markerDbId": 2,
                "defaultDisplayName": "A_01_10002",
                "type": "SNP",
                "synonyms": [
                    "i_01_10001",
                    "popA_10002"
                ],
                "refAlt": [
                    "G",
                    "C"
                ],
                "analysisMethods": [
                    "illumina"
                ]
            }
        ]
    }
}""")

    # end def test_get_markers

# end class MarkerTest
