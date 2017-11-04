from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.crops import CropsViewSet
from brapi.models.crop import Crop


class CropTest(APITestCase):

    def setUp(self):

        Crop.objects.create(data='cassava')
        Crop.objects.create(data='potato')
        Crop.objects.create(data='sweetpotato')
        Crop.objects.create(data='yam')

    # end def setUP


    def test_get_crops(self):

        view = CropsViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/v1/crops/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content.decode('utf-8')` without this.
        self.assertJSONEqual(response.content.decode('utf-8'), """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 4,
            "pageSize": 100
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            "cassava",
            "potato",
            "sweetpotato",
            "yam"
        ]
    }
}""")

    # end def test_get_crops

# end class CropTest
