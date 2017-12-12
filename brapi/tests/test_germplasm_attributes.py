from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class GermplasmAttrsTest(APITestCase):
      
    fixtures = ['crops.json', 'germplasm.json', 'germplasm_attributes.json',
                'germplasm_attribute_values.json', 'germplasm_attribute_categories.json']
    

    def test_get_germplasm_attrs(self):

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
                "determinedDate": "2017-12-11",
                "value": "Present",
                "attributeCode": "RHT",
                "attributeName": "Rht-B1b",
                "germplasmDbId": "1",
                "attributeDbId": "1"
            },
            {
                "determinedDate": "2017-12-11",
                "value": "Absent",
                "attributeCode": "RHT2",
                "attributeName": "Rht-B2b",
                "germplasmDbId": "1",
                "attributeDbId": "1"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/germplasm/1/attributes?pageSize=2', expected)

    # end def test_get_germplasm_attrs


    def test_get_germplasm_attr_cats(self):
        
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
                "attributeCategoryDbId": "1",
                "name": "Morphological"
            },
            {
                "attributeCategoryDbId": "2",
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
            "pageTotal": 5,
            "totalCount": 10,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "code": "RHT",
                "attributeDbId": "1",
                "values": "['Present', 'Absent', 'Heterozygous']",
                "name": "Rht-B1b",
                "uri": "http://www.brapi.org/ontology/MO_123:1000001",
                "description": "Allele of marker 11_4769",
                "datatype": "Categorical",
                "attributeCategoryDbId": "2"
            },
            {
                "code": "RAL6",
                "attributeDbId": "10",
                "values": "['1', '2', '3', '4']",
                "name": "R allele 6",
                "uri": "http://www.brapi.org/ontology/MO_123:1000010",
                "description": "Resistance allele",
                "datatype": "Categorical",
                "attributeCategoryDbId": "4"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/attributes/?pageSize=2', expected)

    # end def test_get_germplasm_attr_avail
    
# end class GermplasmAttrsTest
