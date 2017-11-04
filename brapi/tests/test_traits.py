from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.traits import TraitViewSet
from brapi.models.trait import Trait


class TraitTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database        
        Trait.objects.create(traitDbId='1', traitId='CO_334:0100620', name='Carotenoid content', description='Cassava storage root pulp carotenoid content', observationVariables=['CO_334:0100621', 'CO_334:0100623', 'CO_334:0100623'])
        Trait.objects.create(traitDbId='2', traitId='CO_334:0100621', name='Plant height', description='Plant height', observationVariables=['CO_334:0200001'])

    # end def setUP


    def test_get_traits(self):

        view = TraitViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/b1/Traits/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content` without this.
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
                "traitDbId": 1,
                "traitId": "CO_334:0100620",
                "name": "Carotenoid content",
                "description": "Cassava storage root pulp carotenoid content",
                "observationVariables": [
                    "CO_334:0100621",
                    "CO_334:0100623",
                    "CO_334:0100623"
                ],
                "defaultValue": null
            },
            {
                "traitDbId": 2,
                "traitId": "CO_334:0100621",
                "name": "Plant height",
                "description": "Plant height",
                "observationVariables": [
                    "CO_334:0200001"
                ],
                "defaultValue": null
            }
        ]
    }
}""")

    # end def test_get_traits

# end class TraitTest
