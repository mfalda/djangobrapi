from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from brapi.views import CropViewSet, LocationViewSet
from brapi.models import Crop, Location


class CropTest(APITestCase):
    
    def setUp(self):

        Crop.objects.create(data='cassava')
        Crop.objects.create(data='potato')
        Crop.objects.create(data='sweetpotato')
        Crop.objects.create(data='yam')

    # end def setUP


    def test_get_crops(self):

        view = CropViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/b1/crops/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content` without this.
        self.assertEqual(response.content, b"""
{
	"metadata":{
		"pagination":{
			"currentPage":1,
			"pageTotal":1,
			"totalCount":4,
			"pageSize":100
		},
		"status":[],
		"datafiles":[]
	},
	"result":{
		"data":[
			"cassava",
			"potato",
			"sweetpotato",
			"yam"
		]
	}
}""".replace(b'\n', b'').replace(b'\t', b''))

    # end def test_get_crops

# end class CropTest


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
        request = factory.get('/brapi/b1/locations/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render()
        self.assertEqual(response.content, b"""
{
	"metadata":{
		"pagination":{
			"currentPage":1,
			"pageTotal":1,
			"totalCount":2,
			"pageSize":100
		},
		"status":[],
		"datafiles":[]
	},
	"result":{
		"data":[
			{
				"url":"http://testserver/brapi/v1/locations/1/",
				"locationDbId":"1",
				"locationType":"Storage location",
				"name":"Experimental station San Ramon (CIP)",
				"abbreviation":"CIPSRM-1",
				"countryCode":"PER",
				"countryName":"Peru",
				"latitude":"-11.1275",
				"longitude":"-75.356389",
				"altitude":"828",
				"instituteName":"INRA - GDEC",
				"instituteAdress":"route foo, Clermont Ferrand, France"
			},
			{
				"url":"http://testserver/brapi/v1/locations/2/",
				"locationDbId":"2",
				"locationType":"Breeding location",
				"name":"San Ramon",
				"abbreviation":"CIPSRM-2",
				"countryCode":"PER",
				"countryName":"Peru",
				"latitude":"-11.16116",
				"longitude":"-75.34171",
				"altitude":"964",
				"instituteName":"INRA - GDEC",
				"instituteAdress":"route foo, Clermont Ferrand, France"
			}
		]
	}
}""".replace(b'\n', b'').replace(b'\t', b''))

    # end def test_get_locations

# end class LocationTest
