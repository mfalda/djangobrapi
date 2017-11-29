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
                "comments": "",
                "linkageGroupCount": 10
            },
            {
                "mapDbId": 2,
                "name": "SSR map 2",
                "species": "Ipomoea trifida",
                "type": "Genetic",
                "unit": "cM",
                "publishedDate": "2016-11-15",
                "comments": "none",
                "linkageGroupCount": 10
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
            "pageSize": 100
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
                        "markerCount": 21,
                        "maxPosition": 50
                    },
                    {
                        "linkageGroupId": 2,
                        "markerCount": 12,
                        "maxPosition": 100
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
        test_get(self, '/brapi/v1/maps/1/', expected)
        
    # end def test_get_map


    def test_get_map_data(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 3,
            "totalCount": 5,
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

        test_get(self, '/brapi/v1/maps/1/positions/1?min=10&max=20', expected)
       
    # end def test_get_map_data_by_range

# end class MapsProgramTest
