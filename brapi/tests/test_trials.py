from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class TrialTest(APITestCase):
    
    fixtures = ['crops.json', 'programs.json', 'locations.json',
                'study_types.json', 'studies.json', 'contacts.json',
                'trials_contacts.json', 'trials.json',
                'trials_addInfo.json']
    
    
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
                "endDate": "2013-05-07",
                "studies": [
                    {
                        "studydbid": "1001",
                        "locationDbId": "1",
                        "studyName": "Study 1",
                        "locationName": "Location 1"
                    },
                    {
                        "studydbid": "1002",
                        "locationDbId": "1",
                        "studyName": "Study 2",
                        "locationName": "Location 1"
                    }
                ],
                "programDbId": "1",
                "contacts": [
                    {
                        "contactDbId": "1",
                        "name": "A. Breeder",
                        "instituteName": "Plant Science Institute",
                        "orcid": "0000-0002-0607-8728",
                        "type": "Breeder",
                        "email": "a.breeder@brapi.org"
                    }
                ],
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "trialName": "Peru Yield Trial 1",
                "programName": "Wheat Resistance Program",
                "trialDbId": "101",
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/312953986E3"
                },
                "startDate": "2013-01-01",
                "active": false
            },
            {
                "endDate": "2015-01-15",
                "studies": [
                    {
                        "studydbid": "1003",
                        "locationDbId": "2",
                        "studyName": "Study 3",
                        "locationName": "Location 2"
                    }
                ],
                "programDbId": "1",
                "contacts": [
                    {
                        "contactDbId": "3",
                        "name": "A. Technician",
                        "instituteName": "Plant Science Institute",
                        "orcid": "0000-0002-0607-8731",
                        "type": "Technician",
                        "email": "a.technician@brapi.org"
                    }
                ],
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "trialName": "Peru Yield Trial 2",
                "programName": "Wheat Resistance Program",
                "trialDbId": "102",
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/1234992349"
                },
                "startDate": "2014-01-06",
                "active": false
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
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "endDate": "2013-05-07",
                "studies": [
                    {
                        "studydbid": "1001",
                        "locationDbId": "1",
                        "studyName": "Study 1",
                        "locationName": "Location 1"
                    },
                    {
                        "studydbid": "1002",
                        "locationDbId": "1",
                        "studyName": "Study 2",
                        "locationName": "Location 1"
                    }
                ],
                "programDbId": "1",
                "contacts": [
                    {
                        "contactDbId": "1",
                        "name": "A. Breeder",
                        "instituteName": "Plant Science Institute",
                        "orcid": "0000-0002-0607-8728",
                        "type": "Breeder",
                        "email": "a.breeder@brapi.org"
                    }
                ],
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "trialName": "Peru Yield Trial 1",
                "programName": "Wheat Resistance Program",
                "trialDbId": "101",
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/312953986E3"
                },
                "startDate": "2013-01-01",
                "active": false
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/trials/101/?pageSize=2', expected)

    # end def test_get_trial_details

# end class TrialTest
