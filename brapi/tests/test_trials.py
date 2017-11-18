from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class TrialTest(APITestCase):
    
    fixtures = ['studies.json', 'trials.json']
    
    
    def test_get_trials(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 5,
            "totalCount": 9,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "additionalInfo": {
                    "values": {
                        "donorName": "Donor1",
                        "specialProject": "Project1"
                    }
                },
                "trialDbId": 1,
                "trialName": "Peru Yield Trial",
                "programDbId": 1,
                "name": "CIPHQ",
                "startDate": "2013-01-01",
                "endDate": "2013-07-05",
                "active": false,
                "studies": []
            },
            {
                "additionalInfo": null,
                "trialDbId": 2,
                "trialName": "Peru Genotype Trial",
                "programDbId": 1,
                "name": "CIPHQ",
                "startDate": "2014-06-01",
                "endDate": "2015-01-15",
                "active": false,
                "studies": []
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/trials/?pageSize=2', expected)

    # end def test_get_trials


    def test_get_trial_details(self):

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
                "trialDbId": 1,
                "trialName": "Peru Yield Trial",
                "programDbId": 1,
                "name": "CIPHQ",
                "startDate": "2013-01-01",
                "endDate": "2013-07-05",
                "active": false,
                "studies": []
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/trials/1', expected)

    # end def test_get_trial_details

# end class TrialTest
