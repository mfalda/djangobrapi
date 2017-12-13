from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class MapsTest(APITestCase):
    
    fixtures = ['maps.json', 'map_linkages.json']
    

    def test_get_maps(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 2,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "mapDbId": 1,
                "linkageGroupCount": 19,
                "markerCount": 40,
                "name": "SSR map 1",
                "species": "Ipomoea batatas",
                "type": "Genetic",
                "unit": "cM",
                "publishedDate": "2016-01-06",
                "comments": "10"
            },
            {
                "mapDbId": 2,
                "linkageGroupCount": 21,
                "markerCount": 40,
                "name": "Some Map",
                "species": "Some species",
                "type": "Genetic",
                "unit": "kM",
                "publishedDate": "2008-04-16",
                "comments": "This map contains ..."
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/maps/?pageSize=2', expected)
        
    # end def test_get_maps


    def test_get_map(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 1,
            "totalCount": 1,
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
                "type": "Genetic",
                "unit": "cM",
                "linkageGroups": [
                    {
                        "linkageGroupId": 1,
                        "markerCount": 11,
                        "maxPosition": 50
                    },
                    {
                        "linkageGroupId": 2,
                        "markerCount": 8,
                        "maxPosition": 100
                    },
                    {
                        "linkageGroupId": 1,
                        "markerCount": 10,
                        "maxPosition": 45
                    },
                    {
                        "linkageGroupId": 2,
                        "markerCount": 4,
                        "maxPosition": 24
                    },
                    {
                        "linkageGroupId": 3,
                        "markerCount": 7,
                        "maxPosition": 90
                    }
                ]
            }
        ]
    }
}"""        
        test_get(self, '/brapi/v1/maps/1/?pageSize=2', expected)
        
    # end def test_get_map


    def test_get_map_data(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 6,
            "totalCount": 11,
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
                "linkageGroupId": 1
            },
            {
                "markerDbId": 2,
                "markerName": "m2",
                "location": 20,
                "linkageGroupId": 1
            }
        ]
    }
}"""       
        test_get(self, '/brapi/v1/maps/1/positions/1/?linkageGroupId=1&pageSize=2', expected)
        
    # end def test_get_map_data


    def test_get_map_data_by_range(self):

        expected = """    
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
            {
                "markerDbId": 1,
                "markerName": "m1",
                "location": 10,
                "linkageGroupId": 1
            },
            {
                "markerDbId": 2,
                "markerName": "m2",
                "location": 20,
                "linkageGroupId": 1
            },
            {
                "markerDbId": 21,
                "markerName": "m25",
                "location": 12,
                "linkageGroupId": 1
            },
            {
                "markerDbId": 21,
                "markerName": "m26",
                "location": 15,
                "linkageGroupId": 1
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/maps/1/positions/1?min=10&max=20', expected)
       
    # end def test_get_map_data_by_range

# end class MapsProgramTest
