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
            "totalPages": 5,
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
                        "studyDbId": "1001",
                        "locationDbId": "1",
                        "studyName": "Study 1",
                        "locationName": "Location 1"
                    },
                    {
                        "studyDbId": "1002",
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
                        "studyDbId": "1003",
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


    def test_get_trials_programDbId(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 2,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/312953986E3"
                },
                "startDate": "2013-01-01",
                "programDbId": "1",
                "studies": [
                    {
                        "studyDbId": "1001",
                        "locationDbId": "1",
                        "studyName": "Study 1",
                        "locationName": "Location 1"
                    },
                    {
                        "studyDbId": "1002",
                        "locationDbId": "1",
                        "studyName": "Study 2",
                        "locationName": "Location 1"
                    }
                ],
                "contacts": [
                    {
                        "email": "a.breeder@brapi.org",
                        "contactDbId": "1",
                        "instituteName": "Plant Science Institute",
                        "name": "A. Breeder",
                        "type": "Breeder",
                        "orcid": "0000-0002-0607-8728"
                    }
                ],
                "active": false,
                "trialName": "Peru Yield Trial 1",
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "programName": "Wheat Resistance Program",
                "endDate": "2013-05-07",
                "trialDbId": "101"
            },
            {
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/1234992349"
                },
                "startDate": "2014-01-06",
                "programDbId": "1",
                "studies": [
                    {
                        "studyDbId": "1003",
                        "locationDbId": "2",
                        "studyName": "Study 3",
                        "locationName": "Location 2"
                    }
                ],
                "contacts": [
                    {
                        "email": "a.technician@brapi.org",
                        "contactDbId": "3",
                        "instituteName": "Plant Science Institute",
                        "name": "A. Technician",
                        "type": "Technician",
                        "orcid": "0000-0002-0607-8731"
                    }
                ],
                "active": false,
                "trialName": "Peru Yield Trial 2",
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "programName": "Wheat Resistance Program",
                "endDate": "2015-01-15",
                "trialDbId": "102"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/trials/?programDbId=1&pageSize=2', expected)

    # end def test_get_trials_programDbId


    def test_get_trials_locationDbId(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 1,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/1234992349"
                },
                "startDate": "2014-01-06",
                "programDbId": "1",
                "studies": [
                    {
                        "studyDbId": "1003",
                        "locationDbId": "2",
                        "studyName": "Study 3",
                        "locationName": "Location 2"
                    }
                ],
                "contacts": [
                    {
                        "email": "a.technician@brapi.org",
                        "contactDbId": "3",
                        "instituteName": "Plant Science Institute",
                        "name": "A. Technician",
                        "type": "Technician",
                        "orcid": "0000-0002-0607-8731"
                    }
                ],
                "active": false,
                "trialName": "Peru Yield Trial 2",
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "programName": "Wheat Resistance Program",
                "endDate": "2015-01-15",
                "trialDbId": "102"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/trials/?locationDbId=2&pageSize=2', expected)

    # end def test_get_trials_locationDbId


    def test_get_trials_active(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
            "totalCount": 2,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "studies": [],
                "programName": "P3",
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/125512251"
                },
                "contacts": [],
                "trialDbId": "106",
                "startDate": "2014-09-22",
                "endDate": "2015-03-31",
                "active": true,
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "trialName": "Ghana Yield Trial 3",
                "programDbId": "3"
            },
            {
                "studies": [],
                "programName": "P6",
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/35673236"
                },
                "contacts": [],
                "trialDbId": "109",
                "startDate": "2016-03-24",
                "endDate": "2016-10-21",
                "active": true,
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "trialName": "Demo Yield Trial",
                "programDbId": "6"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/trials/?active=true&pageSize=2', expected)

    # end def test_get_trials_active


    def test_get_trials_NOTactive(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 4,
            "totalCount": 7,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "programDbId": "1",
                "startDate": "2013-01-01",
                "contacts": [
                    {
                        "contactDbId": "1",
                        "orcid": "0000-0002-0607-8728",
                        "type": "Breeder",
                        "name": "A. Breeder",
                        "instituteName": "Plant Science Institute",
                        "email": "a.breeder@brapi.org"
                    }
                ],
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/312953986E3"
                },
                "programName": "Wheat Resistance Program",
                "studies": [
                    {
                        "studyDbId": "1001",
                        "locationDbId": "1",
                        "studyName": "Study 1",
                        "locationName": "Location 1"
                    },
                    {
                        "studyDbId": "1002",
                        "locationDbId": "1",
                        "studyName": "Study 2",
                        "locationName": "Location 1"
                    }
                ],
                "trialDbId": "101",
                "endDate": "2013-05-07",
                "active": false,
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "trialName": "Peru Yield Trial 1"
            },
            {
                "programDbId": "1",
                "startDate": "2014-01-06",
                "contacts": [
                    {
                        "contactDbId": "3",
                        "orcid": "0000-0002-0607-8731",
                        "type": "Technician",
                        "name": "A. Technician",
                        "instituteName": "Plant Science Institute",
                        "email": "a.technician@brapi.org"
                    }
                ],
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/1234992349"
                },
                "programName": "Wheat Resistance Program",
                "studies": [
                    {
                        "studyDbId": "1003",
                        "locationDbId": "2",
                        "studyName": "Study 3",
                        "locationName": "Location 2"
                    }
                ],
                "trialDbId": "102",
                "endDate": "2015-01-15",
                "active": false,
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "trialName": "Peru Yield Trial 2"
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/trials/?active=false&pageSize=2', expected)

    # end def test_get_trials_NOTactive


    def test_get_trial_sortedAsc(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 5,
            "totalCount": 9,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "programName": "P6",
                "trialName": "Demo Yield Trial",
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "startDate": "2016-03-24",
                "endDate": "2016-10-21",
                "active": true,
                "trialDbId": "109",
                "contacts": [],
                "studies": [],
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/35673236"
                },
                "programDbId": "6"
            },
            {
                "programName": "Wheat Improvement Program",
                "trialName": "Ghana Genotype Trial 1",
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "startDate": "2011-01-05",
                "endDate": "2011-12-15",
                "active": false,
                "trialDbId": "103",
                "contacts": [
                    {
                        "name": "B. Technician",
                        "type": "Technician",
                        "instituteName": "Plant Science Institute",
                        "orcid": "0000-0002-0607-8732",
                        "email": "b.technician@brapi.org",
                        "contactDbId": "4"
                    }
                ],
                "studies": [],
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/134591245"
                },
                "programDbId": "2"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/trials/?sortBy=trialName&sortOrder=asc&pageSize=2', expected)

    # end def test_get_trial_sortedAsc


    def test_get_trial_sortedDesc(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 5,
            "totalCount": 9,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "programName": "Wheat Resistance Program",
                "trialName": "Peru Yield Trial 2",
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "startDate": "2014-01-06",
                "endDate": "2015-01-15",
                "active": false,
                "trialDbId": "102",
                "contacts": [
                    {
                        "name": "A. Technician",
                        "type": "Technician",
                        "instituteName": "Plant Science Institute",
                        "orcid": "0000-0002-0607-8731",
                        "email": "a.technician@brapi.org",
                        "contactDbId": "3"
                    }
                ],
                "studies": [
                    {
                        "studyDbId": "1003",
                        "locationDbId": "2",
                        "studyName": "Study 3",
                        "locationName": "Location 2"
                    }
                ],
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/1234992349"
                },
                "programDbId": "1"
            },
            {
                "programName": "Wheat Resistance Program",
                "trialName": "Peru Yield Trial 1",
                "additionalInfo": {
                    "publications": "pmid:345966399",
                    "donorName": "Donor1",
                    "specialProject": "Project1",
                    "collaborator": "NationalPartner1",
                    "fundingUSD": "500000"
                },
                "startDate": "2013-01-01",
                "endDate": "2013-05-07",
                "active": false,
                "trialDbId": "101",
                "contacts": [
                    {
                        "name": "A. Breeder",
                        "type": "Breeder",
                        "instituteName": "Plant Science Institute",
                        "orcid": "0000-0002-0607-8728",
                        "email": "a.breeder@brapi.org",
                        "contactDbId": "1"
                    }
                ],
                "studies": [
                    {
                        "studyDbId": "1001",
                        "locationDbId": "1",
                        "studyName": "Study 1",
                        "locationName": "Location 1"
                    },
                    {
                        "studyDbId": "1002",
                        "locationDbId": "1",
                        "studyName": "Study 2",
                        "locationName": "Location 1"
                    }
                ],
                "datasetAuthorship": {
                    "license": "https://creativecommons.org/licenses/by/4.0",
                    "datasetPUI": "doi:10.15454/312953986E3"
                },
                "programDbId": "1"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/trials/?sortBy=trialName&sortOrder=desc&pageSize=2', expected)

    # end def test_get_trial_sortedDesc


    def test_get_trial_details(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "totalPages": 1,
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
                        "studyDbId": "1001",
                        "locationDbId": "1",
                        "studyName": "Study 1",
                        "locationName": "Location 1"
                    },
                    {
                        "studyDbId": "1002",
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
