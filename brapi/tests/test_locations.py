from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class LocationTest(APITestCase):
 
    fixtures = ['locations.json', 'locations_addInfo.json']


    def test_get_locations(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 9,
            "totalCount": 17,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "locationDbId": 1,
                "locationType": "Storage location",
                "name": "Experimental station San Ramon (CIP)",
                "abbreviation": "CIPSRM-1",
                "countryCode": "PER",
                "countryName": "Peru",
                "latitude": -11.1275,
                "longitude": -75.356389,
                "altitude": "828",
                "instituteName": "INRA - GDEC",
                "instituteAdress": "route foo, Clermont Ferrand, France",
                "additionalInfo": {
                    "values": {
                        " local": "San Ramon",
                        "crops": "potato,sweetpotato",
                        "cont": "South America",
                        "creg": "LAC",
                        "adm3": "San Ramon",
                        "adm2": "Chanchamayo",
                        "adm1": "Junin",
                        "annualTotalPrecipitation": "360",
                        "annualMeanTemperature": "23"
                    }
                }
            },
            {
                "locationDbId": 2,
                "locationType": "Breeding location",
                "name": "San Ramon",
                "abbreviation": "CIPSRM-2",
                "countryCode": "PER",
                "countryName": "Peru",
                "latitude": -11.16116,
                "longitude": -75.34171,
                "altitude": "964",
                "instituteName": "INRA - GDEC",
                "instituteAdress": "route foo, Clermont Ferrand, France",
                "additionalInfo": null
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/locations/?pageSize=2', expected)
        
    # end def test_get_locations


    def test_get_location_details(self):

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
                "latitude": -11.1275,
                "countryName": "Peru",
                "abbreviation": "CIPSRM-1",
                "instituteName": "INRA - GDEC",
                "longitude": -75.356389,
                "altitude": "828",
                "instituteAdress": "route foo, Clermont Ferrand, France",
                "locationType": "Storage location",
                "additionalInfo": {
                    "values": {
                        " local": "San Ramon",
                        "crops": "potato,sweetpotato",
                        "cont": "South America",
                        "creg": "LAC",
                        "adm3": "San Ramon",
                        "adm2": "Chanchamayo",
                        "adm1": "Junin",
                        "annualTotalPrecipitation": "360",
                        "annualMeanTemperature": "23"
                    }
                },
                "locationDbId": 1,
                "countryCode": "PER",
                "name": "Experimental station San Ramon (CIP)"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/locations/1/', expected)
        
    # end def test_get_location_details

# end class LocationTest
