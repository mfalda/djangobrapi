from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class LocationTest(APITestCase):
 
    fixtures = ['crops.json', 'locations.json', 'location_addInfo.json']


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
                "longitude": -75.356389,
                "additionalInfo": {
                    "altern": "SNPEDRO",
                    "local": "NaSARRI",
                    "cont": "Africa",
                    "creg": "SSA",
                    "adm3": "Coviriali",
                    "adm2": "Kassena-Nankana",
                    "adm1": "Serere",
                    "annualTotalPrecipitation": "6.4",
                    "annualMeanTemperature": "19.2"
                },
                "latitude": -11.1275,
                "countryName": "Peru",
                "type": "Storage location",
                "locationDbId": "1",
                "name": "Location 1",
                "abbreviation": "L1",
                "countryCode": "PER",
                "altitude": 828.0,
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteName": "Plant Science Institute"
            },
            {
                "longitude": -73.82075,
                "additionalInfo": {
                    "altern": "SNPEDRO",
                    "local": "NaSARRI",
                    "cont": "Africa",
                    "creg": "SSA",
                    "adm3": "Coviriali",
                    "adm2": "Kassena-Nankana",
                    "adm1": "Serere",
                    "annualTotalPrecipitation": "6.4",
                    "annualMeanTemperature": "19.2"
                },
                "latitude": -11.25847,
                "countryName": "Peru",
                "type": "Breeding location",
                "locationDbId": "10",
                "name": "Location 10",
                "abbreviation": "L10",
                "countryCode": "PER",
                "altitude": 276.0,
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteName": "Plant Science Institute"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/locations/?pageSize=2', expected)
        
    # end def test_get_locations


    def test_get_locations_type(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 4,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "instituteName": "Plant Science Institute",
                "type": "Storage location",
                "latitude": -11.1275,
                "countryName": "Peru",
                "altitude": 828.0,
                "abbreviation": "L1",
                "locationDbId": "1",
                "additionalInfo": {
                    "altern": "SNPEDRO",
                    "local": "NaSARRI",
                    "cont": "Africa",
                    "creg": "SSA",
                    "adm3": "Coviriali",
                    "adm2": "Kassena-Nankana",
                    "adm1": "Serere",
                    "annualTotalPrecipitation": "6.4",
                    "annualMeanTemperature": "19.2"
                },
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "name": "Location 1",
                "countryCode": "PER",
                "longitude": -75.356389
            },
            {
                "instituteName": "Plant Science Institute",
                "type": "Storage location",
                "latitude": 0.529144,
                "countryName": "Uganda",
                "altitude": 1173.0,
                "abbreviation": "L16",
                "locationDbId": "16",
                "additionalInfo": {
                    "altern": "SNPEDRO",
                    "local": "NaSARRI",
                    "cont": "Africa",
                    "creg": "SSA",
                    "adm3": "Coviriali",
                    "adm2": "Kassena-Nankana",
                    "adm1": "Serere",
                    "annualTotalPrecipitation": "6.4",
                    "annualMeanTemperature": "19.2"
                },
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "name": "Location 16",
                "countryCode": "UGA",
                "longitude": 32.61246
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/locations/?locationType=Storage location&pageSize=2', expected)

    # end def test_get_locations_type


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
                "longitude": -75.356389,
                "additionalInfo": {
                    "altern": "SNPEDRO",
                    "local": "NaSARRI",
                    "cont": "Africa",
                    "creg": "SSA",
                    "adm3": "Coviriali",
                    "adm2": "Kassena-Nankana",
                    "adm1": "Serere",
                    "annualTotalPrecipitation": "6.4",
                    "annualMeanTemperature": "19.2"
                },
                "latitude": -11.1275,
                "countryName": "Peru",
                "type": "Storage location",
                "locationDbId": "1",
                "name": "Location 1",
                "abbreviation": "L1",
                "countryCode": "PER",
                "altitude": 828.0,
                "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                "instituteName": "Plant Science Institute"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/locations/1/', expected)
        
    # end def test_get_location_details

# end class LocationTest
