#from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APITestCase


class MapsTest(APITestCase):
    
    fixtures = ['fixtures/maps.json', 'fixtures/map_linkages.json']
    
    def setUp(self):

        # populate the mockup database
        pass
#        m1 = Map.objects.create(mapDbId='1', name='SSR map 1', species='Ipomoea batatas', type='Genetic', unit='cM', publishedDate='2016-01-06', markerCount='10')
#        m2 = Map.objects.create(mapDbId='2', name='SSR map 2', species='Ipomoea trifida', type='Genetic', unit='cM', publishedDate='2016-11-15', markerCount='10', comments='none')
#        
#        MapLinkage.objects.create(mapDbId=m1, markerDbId='1', markerName='m1', location='10', linkageGroupId='1')
#        MapLinkage.objects.create(mapDbId=m1, markerDbId='2', markerName='m2', location='20', linkageGroupId='1')
#        MapLinkage.objects.create(mapDbId=m2, markerDbId='11', markerName='m11', location='0', linkageGroupId='1')
#        MapLinkage.objects.create(mapDbId=m2, markerDbId='12', markerName='m12', location='5', linkageGroupId='1')

    # end def setUP


    def test_get_maps(self):

        #token = Token.objects.get(user__username='marco')
        client = APIClient(enforce_csrf_checks=True)
        #client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = client.get('/brapi/v1/maps?pageSize=2')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content.decode('utf-8')` without this.
        self.assertJSONEqual(response.content.decode('utf-8'), """
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
                "mapDbId": 1,
                "name": "SSR map 1",
                "species": "Ipomoea batatas",
                "type": "Genetic",
                "unit": "cM",
                "publishedDate": "2016-01-06",
                "markerCount": 10,
                "comments": "",
                "linkageGroups": [
                    {
                        "markerDbId": 1,
                        "markerName": "m1",
                        "location": 10,
                        "linkageGroupId": 1,
                        "mapDbId": 1
                    },
                    {
                        "markerDbId": 2,
                        "markerName": "m2",
                        "location": 20,
                        "linkageGroupId": 1,
                        "mapDbId": 1
                    }                    
                ]
            },
            {
                "mapDbId": 2,
                "name": "SSR map 2",
                "species": "Ipomoea trifida",
                "type": "Genetic",
                "unit": "cM",
                "publishedDate": "2016-11-15",
                "markerCount": 10,
                "comments": "none",
                "linkageGroups": [
                    {
                        "markerDbId": 11,
                        "markerName": "m11",
                        "location": 0,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    },
                    {
                        "markerDbId": 12,
                        "markerName": "m12",
                        "location": 5,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    }
                ]
            }                    
        ]
    }
}""")

    # end def test_get_maps


    def test_get_map(self):

        # TODO: implement test_get_map
        pass

    # end def test_get_map

    def test_get_map_data(self):

        #token = Token.objects.get(user__username='marco')
        client = APIClient(enforce_csrf_checks=True)
        #client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = client.get('/brapi/v1/maps/2/positions?pageSize=2')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content.decode('utf-8')` without this.
        self.assertJSONEqual(response.content.decode('utf-8'), """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 20,
            "totalCount": 40,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "markerDbId": 1,
                "markerName": "m1",
                "location": 10,
                "linkageGroupId": 1,
                "mapDbId": 1
            },
            {
                "markerDbId": 2,
                "markerName": "m2",
                "location": 20,
                "linkageGroupId": 1,
                "mapDbId": 1
            }               
        ]
    }
}""")

    # end def test_get_map_data


# end class MapsProgramTest
