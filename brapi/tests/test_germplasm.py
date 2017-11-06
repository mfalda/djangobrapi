from rest_framework.test import APITestCase

from brapi.aux_fun import test_get
from brapi.views.germplasm import GermplasmAttrView


class GermplasmTest(APITestCase):
      
    fixtures = ['germplasm_attrs.json']
    

    def test_get_germplasm(self):

        pass

    # end def test_get_germplasm


    def test_get_germplasm_attrs(self):

        expected = """
[
    {
        "attributeDbId": "1",
        "attributeName": "Morphological",
        "attributeCode": "FLSHORG",
        "value": "Present",
        "dateDetermined": "2016-01-01"
    },
    {
        "attributeDbId": "2",
        "attributeName": "Agronomic",
        "attributeCode": "RHT",
        "value": "Absent",
        "dateDetermined": "2016-01-01"
    },
    {
        "attributeDbId": "3",
        "attributeName": "Biotic stress",
        "attributeCode": "WEV",
        "value": "Present",
        "dateDetermined": "2016-01-01"
    }
]"""
        test_get(self, GermplasmAttrView, '/brapi/v1/germplasm/1/attributes', expected, True)

    # end def test_get_germplasm_attrs

# end class GermplasmTest
