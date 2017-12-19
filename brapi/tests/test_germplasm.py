from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class GermplasmTest(APITestCase):
      
    fixtures = ['crops.json', 'locations.json', 'programs.json', 'trials.json', 'study_types.json',
                'studies.json', 'markerprofiles.json', 'germplasm.json', 'taxon_xrefs.json',
                'taxon_xref_germplasm.json', 'donors.json', 'pedigrees.json']
    

    def test_get_germplasm_details(self):

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
                "species": "novus",
                "subtaxaAuthority": "N",
                "defaultDisplayName": "G000001",
                "instituteName": "INST1",
                "donors": [
                    {
                        "donorAccessionNumber": "BRA001001",
                        "donorInstituteCode": "BRA001",
                        "donorGermplasmPUI": "http://bra/accession/BRA001001"
                    }
                ],
                "germplasmName": "Name001",
                "synonyms": [
                    "landrace 1"
                ],
                "seedSource": "open pollination",
                "speciesAuthority": "L",
                "acquisitionDate": "1984-01-01",
                "typeOfGermplasmStorageCode": [
                    13
                ],
                "genus": "Fructus",
                "subtaxa": "subtaxa",
                "pedigree": "landrace",
                "taxonIds": [
                    {
                        "ncbiTaxon": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "ciradTaxon": "23-E"
                    }
                ],
                "germplasmDbId": "1",
                "accessionNumber": "A000001",
                "biologicalStatusOfAccessionCode": "300",
                "countryOfOriginCode": "COUNTRY1",
                "commonCropName": "banana",
                "instituteCode": "PER001",
                "germplasmPUI": "http://pui.per/accession/A000001"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/germplasm/1/?pageSize=2', expected)

    # end def test_get_germplasm_details


    def test_get_germplasm_pedigrees(self):

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
                "pedigreeDbId": "1",
                "pedigree": "Cree / Bonanza",
                "defaultDisplayName": "Pahang",
                "germplasmDbId": "1",
                "parent1DbId": "2",
                "parent2DbId": "3"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/germplasm/1/pedigree?pageSize=2', expected)

    # end def test_get_germplasm_pedigrees


    def test_get_germplasm_markerprofiles(self):

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
                "germplasmDbId": "1",
                "markerprofileDbIds": [
                    1,
                    2
                ]
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/germplasm/1/markerprofiles?pageSize=2', expected)

        # end def test_get_germplasm_markerprofiles

# end class GermplasmTest


class GermplasmSearchTest(APITestCase):

    fixtures = ['crops.json', 'locations.json', 'programs.json', 'trials.json', 'study_types.json',
                'studies.json', 'markerprofiles.json', 'germplasm.json', 'taxon_xrefs.json',
                'taxon_xref_germplasm.json', 'donors.json', 'pedigrees.json']


    def test_get_germplasm_search(self):

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
                "accessionNumber": "A000001",
                "biologicalStatusOfAccessionCode": "300",
                "taxonIds": [
                    {
                        "ncbiTaxon": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "ciradTaxon": "23-E"
                    }
                ],
                "synonyms": [
                    "landrace 1"
                ],
                "speciesAuthority": "L",
                "acquisitionDate": "1984-01-01",
                "donors": [
                    {
                        "donorAccessionNumber": "BRA001001",
                        "donorInstituteCode": "BRA001",
                        "donorGermplasmPUI": "http://bra/accession/BRA001001"
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A000001",
                "defaultDisplayName": "G000001",
                "instituteName": "INST1",
                "germplasmName": "Name001",
                "species": "novus",
                "countryOfOriginCode": "COUNTRY1",
                "seedSource": "open pollination",
                "subtaxa": "subtaxa",
                "pedigree": "landrace",
                "genus": "Fructus",
                "instituteCode": "PER001",
                "germplasmDbId": "1",
                "commonCropName": "banana",
                "typeOfGermplasmStorageCode": [
                    13
                ],
                "subtaxaAuthority": "N"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/germplasm-search?germplasmDbId=1&pageSize=2', expected)

    # end def test_get_germplasm_search


    def test_get_germplasm_search_name(self):

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
                "accessionNumber": "A000002",
                "biologicalStatusOfAccessionCode": "300",
                "taxonIds": [],
                "synonyms": [
                    "landrace 2"
                ],
                "speciesAuthority": "L",
                "acquisitionDate": "1984-01-01",
                "donors": [
                    {
                        "donorAccessionNumber": "ECU001001",
                        "donorInstituteCode": "ECU001",
                        "donorGermplasmPUI": "http://ecu/accession/ECU001001"
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A000002",
                "defaultDisplayName": "G000002",
                "instituteName": "INST1",
                "germplasmName": "Name002",
                "species": "novus",
                "countryOfOriginCode": "COUNTRY1",
                "seedSource": "open pollination",
                "subtaxa": "subtaxa",
                "pedigree": "landrace",
                "genus": "Fructus",
                "instituteCode": "PER001",
                "germplasmDbId": "2",
                "commonCropName": "banana",
                "typeOfGermplasmStorageCode": [
                    20
                ],
                "subtaxaAuthority": "N"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/germplasm-search?germplasmName=Name002&pageSize=2', expected)

    # end def test_get_germplasm_search_name


    def test_get_germplasm_search_PUI(self):

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
                "accessionNumber": "A000001",
                "biologicalStatusOfAccessionCode": "300",
                "taxonIds": [
                    {
                        "ncbiTaxon": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "ciradTaxon": "23-E"
                    }
                ],
                "synonyms": [
                    "landrace 1"
                ],
                "speciesAuthority": "L",
                "acquisitionDate": "1984-01-01",
                "donors": [
                    {
                        "donorAccessionNumber": "BRA001001",
                        "donorInstituteCode": "BRA001",
                        "donorGermplasmPUI": "http://bra/accession/BRA001001"
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A000001",
                "defaultDisplayName": "G000001",
                "instituteName": "INST1",
                "germplasmName": "Name001",
                "species": "novus",
                "countryOfOriginCode": "COUNTRY1",
                "seedSource": "open pollination",
                "subtaxa": "subtaxa",
                "pedigree": "landrace",
                "genus": "Fructus",
                "instituteCode": "PER001",
                "germplasmDbId": "1",
                "commonCropName": "banana",
                "typeOfGermplasmStorageCode": [
                    13
                ],
                "subtaxaAuthority": "N"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/germplasm-search?germplasmPUI=http://pui.per/accession/A000001&pageSize=2', expected)

    # end def test_get_germplasm_search_PUI


    def test_post_germplasm_search(self):

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
                "accessionNumber": "A000001",
                "biologicalStatusOfAccessionCode": "300",
                "taxonIds": [
                    {
                        "ncbiTaxon": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "ciradTaxon": "23-E"
                    }
                ],
                "synonyms": [
                    "landrace 1"
                ],
                "speciesAuthority": "L",
                "acquisitionDate": "1984-01-01",
                "donors": [
                    {
                        "donorAccessionNumber": "BRA001001",
                        "donorInstituteCode": "BRA001",
                        "donorGermplasmPUI": "http://bra/accession/BRA001001"
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A000001",
                "defaultDisplayName": "G000001",
                "instituteName": "INST1",
                "germplasmName": "Name001",
                "species": "novus",
                "countryOfOriginCode": "COUNTRY1",
                "seedSource": "open pollination",
                "subtaxa": "subtaxa",
                "pedigree": "landrace",
                "genus": "Fructus",
                "instituteCode": "PER001",
                "germplasmDbId": "1",
                "commonCropName": "banana",
                "typeOfGermplasmStorageCode": [
                    13
                ],
                "subtaxaAuthority": "N"
            }
        ]
    }
}"""
        params = {
            "germplasmDbIds": [1]
        }
        
        test_post(self, '/brapi/v1/germplasm-search?pageSize=2', params, expected)

    # end def test_post_germplasm_search


    def test_post_germplasm_search_name(self):

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
                "accessionNumber": "A000001",
                "biologicalStatusOfAccessionCode": "300",
                "taxonIds": [
                    {
                        "ncbiTaxon": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "ciradTaxon": "23-E"
                    }
                ],
                "synonyms": [
                    "landrace 1"
                ],
                "speciesAuthority": "L",
                "acquisitionDate": "1984-01-01",
                "donors": [
                    {
                        "donorAccessionNumber": "BRA001001",
                        "donorInstituteCode": "BRA001",
                        "donorGermplasmPUI": "http://bra/accession/BRA001001"
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A000001",
                "defaultDisplayName": "G000001",
                "instituteName": "INST1",
                "germplasmName": "Name001",
                "species": "novus",
                "countryOfOriginCode": "COUNTRY1",
                "seedSource": "open pollination",
                "subtaxa": "subtaxa",
                "pedigree": "landrace",
                "genus": "Fructus",
                "instituteCode": "PER001",
                "germplasmDbId": "1",
                "commonCropName": "banana",
                "typeOfGermplasmStorageCode": [
                    13
                ],
                "subtaxaAuthority": "N"
            }
        ]
    }
}"""
        params = {
            "germplasmNames": ["Name001"]
        }

        test_post(self, '/brapi/v1/germplasm-search?pageSize=2', params, expected)

    # end def test_post_germplasm_search_name


    def test_post_germplasm_search_PUI(self):

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
                "accessionNumber": "A000001",
                "biologicalStatusOfAccessionCode": "300",
                "taxonIds": [
                    {
                        "ncbiTaxon": "http://purl.obolibrary.org/obo/NCBITaxon_4641"
                    },
                    {
                        "ciradTaxon": "23-E"
                    }
                ],
                "synonyms": [
                    "landrace 1"
                ],
                "speciesAuthority": "L",
                "acquisitionDate": "1984-01-01",
                "donors": [
                    {
                        "donorAccessionNumber": "BRA001001",
                        "donorInstituteCode": "BRA001",
                        "donorGermplasmPUI": "http://bra/accession/BRA001001"
                    }
                ],
                "germplasmPUI": "http://pui.per/accession/A000001",
                "defaultDisplayName": "G000001",
                "instituteName": "INST1",
                "germplasmName": "Name001",
                "species": "novus",
                "countryOfOriginCode": "COUNTRY1",
                "seedSource": "open pollination",
                "subtaxa": "subtaxa",
                "pedigree": "landrace",
                "genus": "Fructus",
                "instituteCode": "PER001",
                "germplasmDbId": "1",
                "commonCropName": "banana",
                "typeOfGermplasmStorageCode": [
                    13
                ],
                "subtaxaAuthority": "N"
            }
        ]
    }
}"""
        params = {
            "germplasmPUIs": ["http://pui.per/accession/A000001"]
        }

        test_post(self, '/brapi/v1/germplasm-search?pageSize=2', params, expected)

    # end def test_post_germplasm_search_PUI

# end class GermplasmSearchTest
