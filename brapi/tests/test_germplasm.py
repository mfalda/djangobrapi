from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.germplasm import GermplasmView
from brapi.models.germplasm import Germplasm


class GermplasmTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database
        Germplasm.objects.create(germplasmDbId='1', defaultDisplayName='G000001',
                                 accessionNumber='A000001', germplasmName='Name001',
                                 germplasmPUI='http://data.cipotato.org/accession/A000001',
                                 pedigree='landrace', germplasmSeedSource='open pollination', 
                                 synonyms='landrace 1', commonCropName='sweetpotato', 
                                 instituteCode='PER001', instituteName='CIP', 
                                 biologicalStatusOfAccessionCode='300', 
                                 countryOfOriginCode='BRA', 
                                 typeOfGermplasmStorageCode='13', genus='Ipomoea', 
                                 species='batatas', speciesAuthority='L', subtaxa='', 
                                 subtaxaAuthority='', donors='1', acquisitionDate='1984-01-01', 
                                 taxonIDs=['{"ncbiTaxon":"http://purl.obolibrary.org/obo/NCBITaxon_4641"}', '{"ciradTaxon":"23-E"}'])

        Germplasm.objects.create(germplasmDbId='2', defaultDisplayName='G000002',
                                 accessionNumber='A000002', germplasmName='Name002',
                                 germplasmPUI='http://data.cipotato.org/accession/A000002', 
                                 pedigree='landrace', germplasmSeedSource='open pollination',
                                 synonyms='landrace 2', commonCropName='sweetpotato', 
                                 instituteCode='PER001', instituteName='CIP', 
                                 biologicalStatusOfAccessionCode='300', 
                                 countryOfOriginCode='ECU', 
                                 typeOfGermplasmStorageCode='20', genus='Ipomoea', 
                                 species='batatas', speciesAuthority='L', subtaxa='', 
                                 subtaxaAuthority='', donors='2', acquisitionDate='1984-01-02', 
                                 taxonIDs=['{"ncbiTaxon":"http://purl.obolibrary.org/obo/NCBITaxon_4641"}', '{"ciradTaxon":"23-E"}'])

    # end def setUP


    def test_get_germplasm(self):

        view = GermplasmView.as_view()

        factory = APIRequestFactory()
        request = factory.get('/brapi/v1/germplasms/1/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content.decode('utf-8')` without this.
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
                "synonyms": [
                    "landrace 1"
                ],
                "donors": [
                    "1"
                ],
                "germplasmDbId": 1,
                "defaultDisplayName": "G000001",
                "accessionNumber": "A000001",
                "germplasmName": "Name001",
                "germplasmPUI": "http://data.cipotato.org/accession/A000001",
                "pedigree": "landrace",
                "germplasmSeedSource": "open pollination",
                "commonCropName": "sweetpotato",
                "instituteCode": "PER001",
                "instituteName": "CIP",
                "biologicalStatusOfAccessionCode": 300,
                "countryOfOriginCode": "BRA",
                "typeOfGermplasmStorageCode": "13",
                "genus": "Ipomoea",
                "species": "batatas",
                "speciesAuthority": "L",
                "subtaxa": "",
                "subtaxaAuthority": "",
                "acquisitionDate": "1984-01-01",
                "taxonIds": "\"{\"\"ncbiTaxon\"\":\"\"http://purl.obolibrary.org/obo/NCBITaxon_4641\"\"}; {\"\"ciradTaxon\"\":\"\"23-E\"\"}\""
            },
            {
                "synonyms": [
                    "landrace 2"
                ],
                "donors": [
                    "2"
                ],
                "germplasmDbId": 2,
                "defaultDisplayName": "G000002",
                "accessionNumber": "A000002",
                "germplasmName": "Name002",
                "germplasmPUI": "http://data.cipotato.org/accession/A000002",
                "pedigree": "landrace",
                "germplasmSeedSource": "open pollination",
                "commonCropName": "sweetpotato",
                "instituteCode": "PER001",
                "instituteName": "CIP",
                "biologicalStatusOfAccessionCode": 300,
                "countryOfOriginCode": "ECU",
                "typeOfGermplasmStorageCode": "20",
                "genus": "Ipomoea",
                "species": "batatas",
                "speciesAuthority": "L",
                "subtaxa": "",
                "subtaxaAuthority": "",
                "acquisitionDate": "1984-01-02",
                "taxonIds": "\"{\"\"ncbiTaxon\"\":\"\"http://purl.obolibrary.org/obo/NCBITaxon_4641\"\"}; {\"\"ciradTaxon\"\":\"\"23-E\"\"}\""
            }
        ]
    }
}""")

    # end def test_get_germplasm

# end class GermplasmTest
