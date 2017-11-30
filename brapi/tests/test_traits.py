from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class TraitTest(APITestCase):
    
    fixtures = ['crops.json', 'traits.json']
    

    def test_get_traits(self):

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
                "traitDbId": 1,
                "traitId": "CO_334:0100620",
                "name": "Carotenoid content",
                "description": "Cassava storage root pulp carotenoid content",
                "observationVariables": [
                    "CO_334:0100621",
                    "CO_334:0100623",
                    "CO_334:0100623"
                ]
            },
            {
                "traitDbId": 2,
                "traitId": "CO_334:0100621",
                "name": "Plant height",
                "description": "Plant height",
                "observationVariables": [
                    "CO_334:0200001"
                ]
            }
        ]
    }
}"""
            
        test_get(self, '/brapi/v1/traits/?pageSize=2', expected)

    # end def test_get_traits


    def test_get_trait_details(self):

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
                "traitDbId": 1,
                "traitId": "CO_334:0100620",
                "name": "Carotenoid content",
                "description": "Cassava storage root pulp carotenoid content",
                "observationVariables": [
                    "CO_334:0100621",
                    "CO_334:0100623",
                    "CO_334:0100623"
                ]
            }
        ]
    }
}"""
            
        test_get(self, '/brapi/v1/traits/1', expected)

    # end def test_get_trait_details
    
# end class TraitTest
