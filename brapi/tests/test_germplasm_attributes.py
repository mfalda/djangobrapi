from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class GermplasmAttrsTest(APITestCase):
      
    fixtures = ['germplasm_attrs.json', 'germplasm_attrs_list.json', 
                'germplasm_attrs_avail.json']
    

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
        test_get(self, '/brapi/v1/germplasm/1/attributes', expected)

    # end def test_get_germplasm_attrs


    def test_get_germplasm_attr_cats(self):
        
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
                "attributeCategoryDbId": 1,
                "name": "Morphological"
            },
            {
                "attributeCategoryDbId": 2,
                "name": "Agronomic"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/attributes/categories/?pageSize=2', expected)

    # end def test_get_germplasm_attr_cats
    
    
    def test_get_germplasm_attr_avail(self):
        
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
                "attributeCategoryDbId": 1,
                "code": "RHT",
                "uri": "http://www.cropontology.org/rdf/CO_321:0000020",
                "name": "Rht-B1b",
                "description": "Allele of marker 11_4769, diagnostic for allele b of reduced-height gene Rht-B1''",
                "datatype": "Categorical",
                "values": [
                    "Present",
                    "Absent",
                    "Heterozygous"
                ]
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/attributes/', expected)

    # end def test_get_germplasm_attr_avail
    
# end class GermplasmAttrsTest
