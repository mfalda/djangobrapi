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
                    },
                    {
                        "markerDbId": 3,
                        "markerName": "m3",
                        "location": 30,
                        "linkageGroupId": 1,
                        "mapDbId": 1
                    },
                    {
                        "markerDbId": 4,
                        "markerName": "m4",
                        "location": 40,
                        "linkageGroupId": 1,
                        "mapDbId": 1
                    },
                    {
                        "markerDbId": 5,
                        "markerName": "m5",
                        "location": 50,
                        "linkageGroupId": 1,
                        "mapDbId": 1
                    },
                    {
                        "markerDbId": 6,
                        "markerName": "m6",
                        "location": 0,
                        "linkageGroupId": 2,
                        "mapDbId": 1
                    },
                    {
                        "markerDbId": 7,
                        "markerName": "m7",
                        "location": 25,
                        "linkageGroupId": 2,
                        "mapDbId": 1
                    },
                    {
                        "markerDbId": 8,
                        "markerName": "m8",
                        "location": 50,
                        "linkageGroupId": 2,
                        "mapDbId": 1
                    },
                    {
                        "markerDbId": 9,
                        "markerName": "m9",
                        "location": 75,
                        "linkageGroupId": 2,
                        "mapDbId": 1
                    },
                    {
                        "markerDbId": 10,
                        "markerName": "m10",
                        "location": 100,
                        "linkageGroupId": 2,
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
                    },
                    {
                        "markerDbId": 13,
                        "markerName": "m13",
                        "location": 10,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    },
                    {
                        "markerDbId": 14,
                        "markerName": "m14",
                        "location": 15,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    },
                    {
                        "markerDbId": 15,
                        "markerName": "m15",
                        "location": 20,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    },
                    {
                        "markerDbId": 16,
                        "markerName": "m16",
                        "location": 25,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    },
                    {
                        "markerDbId": 17,
                        "markerName": "m17",
                        "location": 30,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    },
                    {
                        "markerDbId": 18,
                        "markerName": "m18",
                        "location": 35,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    },
                    {
                        "markerDbId": 19,
                        "markerName": "m19",
                        "location": 40,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    },
                    {
                        "markerDbId": 20,
                        "markerName": "m20",
                        "location": 45,
                        "linkageGroupId": 1,
                        "mapDbId": 2
                    }
                ]
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/maps/?pageSize=2', expected)
        
    # end def test_get_maps


    def test_get_map(self):

        expected = """
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
        },
        {
            "markerDbId": 3,
            "markerName": "m3",
            "location": 30,
            "linkageGroupId": 1,
            "mapDbId": 1
        },
        {
            "markerDbId": 4,
            "markerName": "m4",
            "location": 40,
            "linkageGroupId": 1,
            "mapDbId": 1
        },
        {
            "markerDbId": 5,
            "markerName": "m5",
            "location": 50,
            "linkageGroupId": 1,
            "mapDbId": 1
        },
        {
            "markerDbId": 6,
            "markerName": "m6",
            "location": 0,
            "linkageGroupId": 2,
            "mapDbId": 1
        },
        {
            "markerDbId": 7,
            "markerName": "m7",
            "location": 25,
            "linkageGroupId": 2,
            "mapDbId": 1
        },
        {
            "markerDbId": 8,
            "markerName": "m8",
            "location": 50,
            "linkageGroupId": 2,
            "mapDbId": 1
        },
        {
            "markerDbId": 9,
            "markerName": "m9",
            "location": 75,
            "linkageGroupId": 2,
            "mapDbId": 1
        },
        {
            "markerDbId": 10,
            "markerName": "m10",
            "location": 100,
            "linkageGroupId": 2,
            "mapDbId": 1
        }
    ]
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
}"""

        test_get(self, '/brapi/v1/maps/1/positions/1?min=10&max=20', expected)
       
    # end def test_get_map_data_by_range

# end class MapsProgramTest
