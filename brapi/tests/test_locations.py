from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.locations import LocationViewSet
from brapi.models.location import Location


class LocationTest(APITestCase):
 
    def setUp(self):

        Location.objects.create(locationDbId='1',
                     locationType='Storage location',
                     name='Experimental station San Ramon (CIP)',
                     abbreviation='CIPSRM-1',
                     countryCode='PER',
                     countryName='Peru',
                     latitude='-11.1275',
                     longitude='-75.356389',
                     altitude='828',
                     instituteName='INRA - GDEC',
                     instituteAdress='route foo, Clermont Ferrand, France')
        Location.objects.create(locationDbId='2',
                     locationType='Breeding location',
                     name='San Ramon',
                     abbreviation='CIPSRM-2',
                     countryCode='PER',
                     countryName='Peru',
                     latitude='-11.16116',
                     longitude='-75.34171',
                     altitude='964',
                     instituteName='INRA - GDEC',
                     instituteAdress='route foo, Clermont Ferrand, France')

    # end def setUP


    def test_get_locations(self):

        view = LocationViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/v1/locations/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render()
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
                "locationDbId": "1",
                "locationType": "Storage location",
                "name": "Experimental station San Ramon (CIP)",
                "abbreviation": "CIPSRM-1",
                "countryCode": "PER",
                "countryName": "Peru",
                "latitude": -11.1275,
                "longitude": -75.356389,
                "altitude": "828",
                "instituteName": "INRA - GDEC",
                "instituteAdress": "route foo, Clermont Ferrand, France"
            },
            {
                "locationDbId": "2",
                "locationType": "Breeding location",
                "name": "San Ramon",
                "abbreviation": "CIPSRM-2",
                "countryCode": "PER",
                "countryName": "Peru",
                "latitude": -11.16116,
                "longitude": -75.34171,
                "altitude": "964",
                "instituteName": "INRA - GDEC",
                "instituteAdress": "route foo, Clermont Ferrand, France"
            }
        ]
    }
}""")

    # end def test_get_locations

# end class LocationTest
