from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class GermplasmTest(APITestCase):
      
    fixtures = ['germplasm_markerprofiles.json', 'germplasm.json', 
                'taxa.json', 'pedigrees.json']
    

    def test_get_germplasm_details(self):

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
                "germplasmDbId": 1,
                "defaultDisplayName": "G000001",
                "accessionNumber": "A000001",
                "germplasmName": "Name001",
                "germplasmPUI": "http://data.cipotato.org/accession/A000001",
                "pedigree": "landrace",
                "germplasmSeedSource": "open pollination",
                "synonyms": [
                    "landrace 1"
                ],
                "commonCropName": "sweetpotato",
                "instituteCode": "PER001",
                "instituteName": "CIP",
                "biologicalStatusOfAccessionCode": 300,
                "countryOfOriginCode": "BRA",
                "typeOfGermplasmStorageCode": "['13']",
                "genus": "Ipomoea",
                "species": "batatas",
                "speciesAuthority": "L",
                "subtaxa": "",
                "subtaxaAuthority": "",
                "donors": [
                    "1"
                ],
                "acquisitionDate": "1984-01-01",
                "taxonIds": {
                    "ncbiTaxon": "http://purl.obolibrary.org/obo/NCBITaxon_4641",
                    "ciradTaxon": "23-E"
                }
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/germplasm/1', expected)

    # end def test_get_germplasm_details


    def test_get_germplasm_search(self):

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
                "germplasmDbId": 1,
                "defaultDisplayName": "G000001",
                "accessionNumber": "A000001",
                "germplasmName": "Name001",
                "germplasmPUI": "http://data.cipotato.org/accession/A000001",
                "pedigree": "landrace",
                "germplasmSeedSource": "open pollination",
                "synonyms": [
                    "landrace 1"
                ],
                "commonCropName": "sweetpotato",
                "instituteCode": "PER001",
                "instituteName": "CIP",
                "biologicalStatusOfAccessionCode": 300,
                "countryOfOriginCode": "BRA",
                "typeOfGermplasmStorageCode": "['13']",
                "genus": "Ipomoea",
                "species": "batatas",
                "speciesAuthority": "L",
                "subtaxa": "",
                "subtaxaAuthority": "",
                "donors": [
                    "1"
                ],
                "acquisitionDate": "1984-01-01",
                "taxonIds": {
                    "ncbiTaxon": "http://purl.obolibrary.org/obo/NCBITaxon_4641",
                    "ciradTaxon": "23-E"
                }
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/germplasm-search?germplasmName=Name001', expected)

    # end def test_get_germplasm_search
        
    
    def test_post_search(self):

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
                "germplasmDbId": 1,
                "defaultDisplayName": "G000001",
                "accessionNumber": "A000001",
                "germplasmName": "Name001",
                "germplasmPUI": "http://data.cipotato.org/accession/A000001",
                "pedigree": "landrace",
                "germplasmSeedSource": "open pollination",
                "synonyms": [
                    "landrace 1"
                ],
                "commonCropName": "sweetpotato",
                "instituteCode": "PER001",
                "instituteName": "CIP",
                "biologicalStatusOfAccessionCode": 300,
                "countryOfOriginCode": "BRA",
                "typeOfGermplasmStorageCode": "['13']",
                "genus": "Ipomoea",
                "species": "batatas",
                "speciesAuthority": "L",
                "subtaxa": "",
                "subtaxaAuthority": "",
                "donors": [
                    "1"
                ],
                "acquisitionDate": "1984-01-01",
                "taxonIds": {
                    "ncbiTaxon": "http://purl.obolibrary.org/obo/NCBITaxon_4641",
                    "ciradTaxon": "23-E"
                }
            }
        ]
    }
}"""
        params = {
            "germplasmDbId": [1]
        }
        
        test_post(self, '/brapi/v1/germplasm-search', params, expected)

    # end def test_post_search
    
    
    def test_get_germplasm_pedigrees(self):

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
                "germplasmDbId": 1,
                "defaultDisplayName": "Pahang",
                "pedigree": "Cree / Bonanza",
                "parent1Id": 166,
                "parent2Id": 143
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/germplasm/1/pedigree', expected)

    # end def test_get_germplasm_pedigrees
    
    
    def test_get_germplasm_markerprofiles(self):

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
                "germplasmDbId": 1,
                "defaultDisplayName": "Pahang",
                "pedigree": "Cree / Bonanza",
                "parent1Id": 166,
                "parent2Id": 143
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/germplasm/1/pedigree', expected)

    # end def test_get_germplasm_markerprofiles
    
# end class GermplasmTest
