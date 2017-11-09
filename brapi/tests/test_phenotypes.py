from rest_framework.test import APITestCase

from brapi.aux_fun import test_post


class PhenotypeTest(APITestCase):
    
    fixtures = ['obs_vvalues.json',
                'obs_methods.json', 'obs_scales.json', 
                'obs_traits.json', 'obs_variables.json', 
                'observations.json', 'phenotypes.json']
    
    
    def test_post_search(self):

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
                "observationUnitDbId": "2016-Maugio-34-575-abc-123",
                "observationLevel": "plot",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "plantNumber": null,
                "blockNumber": 2,
                "replicate": null,
                "observationUnitName": "2016-Maugio-34-575",
                "germplasmDbId": "doi:10.155454/12349537E12",
                "germplasmName": "IR-8",
                "studyDbId": "YieldStudy2015-5",
                "studyName": "Yield wheat 2015",
                "studyLocationDbId": "mtp-north-32",
                "studyLocation": "Montpellier",
                "programName": "Whealbi",
                "X": 5,
                "Y": 15,
                "entryType": null,
                "entryNumber": null,
                "treatments": 1,
                "observationUnitXref": 1,
                "observations": 153453453
            },
            {
                "observationUnitDbId": "2016-Maugio-34-575-abc-123",
                "observationLevel": "plot",
                "observationLevels": "bloc:2,subBloc:1,plot:2016-Maugio-34-575-abc-123",
                "plotNumber": "2016-Maugio-34-575-abc-123",
                "plantNumber": null,
                "blockNumber": 2,
                "replicate": null,
                "observationUnitName": "2016-Maugio-34-575",
                "germplasmDbId": "doi:10.155454/12349537E12",
                "germplasmName": "IR-8",
                "studyDbId": "YieldStudy2015-5",
                "studyName": "Yield wheat 2015",
                "studyLocationDbId": "mtp-north-32",
                "studyLocation": "Montpellier",
                "programName": "Whealbi",
                "X": 5,
                "Y": 15,
                "entryType": null,
                "entryNumber": null,
                "treatments": 1,
                "observationUnitXref": 1,
                "observations": 23453454345
            }
        ]
    }
}"""
        params = {
            "observationUnitDbIds": ["2016-Maugio-34-575-abc-123"],
            "pageSize": 2
        }

        test_post(self, '/brapi/v1/phenotypes-search', params, expected)

    # end def test_post_search

# end class PhenotypeTest
