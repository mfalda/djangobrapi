from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class CropTest(APITestCase):

    fixtures = ['crops.json']
    

    def test_get_crops(self):

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
            "grape",
            "apple"
        ]
    }
}"""
    
        test_get(self, '/brapi/v1/crops/?pageSize=2', expected)

    # end def test_get_crops

# end class CropTest
