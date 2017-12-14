from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class StudyTest(APITestCase):
    
    fixtures = ['crops.json', 'programs.json', 'trials.json', 'locations.json', 'contacts.json',
                'location_addInfo.json', 'study_types.json', 'studies.json', 'seasons.json',
                'study_observation_levels.json', 'study_seasons.json', 'datalinks.json',
                'study_contacts.json', 'study_types.json', 'study_addInfo.json',
                'germplasm.json', 'observation_units.json', 'observation_units_addInfo.json']
    

    def test_get_obs_levels(self):

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
            "plant",
            "plot"
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/observationLevels/?pageSize=2', expected)
        
    # end def test_get_obs_levels
    

    def test_get_seasons(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 3,
            "totalCount": 5,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "year": "2013",
                "season": "Spring",
                "seasonDbId": "1"
            },
            {
                "year": "2011",
                "season": "Fall",
                "seasonDbId": "2"
            }
        ]
    }
}"""
       
        test_get(self, '/brapi/v1/seasons/?pageSize=2', expected)
        
    # end def test_get_seasons
    
    
    def test_get_types(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageSize": 100,
            "totalCount": 3,
            "pageTotal": 1
        },
        "datafiles": [],
        "status": []
    },
    "result": {
        "data": [
            {
                "name": "Crossing Nursery",
                "description": "Description for Nursery study type"
            },
            {
                "name": "Genotype",
                "description": "Description for Genotyping study type"
            },
            {
                "name": "Yield study",
                "description": "Description for yield study type"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/studyTypes/', expected)
       
    # end def test_get_types
    
    
    def test_get_obs_unit_details(self):

        expected = """
{
}"""
        # test_get(self, '/brapi/v1/studies/1001/observationunits/?pageSize=2', expected)
        self.assertJSONEqual("{}", expected)
        
    # end def test_get_obs_unit_details 
        
    
    def test_get_plot_layout_details(self):

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
                "blockNumber": "1",
                "Y": "1",
                "additionalInfo": {
                    "publications": "pmid:210494013"
                },
                "X": "1",
                "germplasmDbId": "1",
                "observationUnitDbId": "1",
                "observationLevel": "plot",
                "entryType": "test",
                "germplasmName": "Name001",
                "studyDbId": "1001",
                "replicate": "0",
                "observationUnitName": "Plot 1"
            },
            {
                "blockNumber": "1",
                "Y": "1",
                "additionalInfo": {
                    "publications": "pmid:210494013"
                },
                "X": "1",
                "germplasmDbId": "1",
                "observationUnitDbId": "2",
                "observationLevel": "plant",
                "entryType": "test",
                "germplasmName": "Name001",
                "studyDbId": "1001",
                "replicate": "0",
                "observationUnitName": "Plant 1"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/studies/1001/layout/?pageSize=2', expected)
        
    # end def test_get_plot_layout_details 


    def test_get_obsUnit_by_variableID(self):

        expected = """  
{
}"""

        # test_get(self, '/brapi/v1/studies/1001/observations/?pageSize=2', expected)
        self.assertJSONEqual("{}", expected)

    # end def test_get_obsUnit_by_variableID


    def test_get_search(self):

        expected = """  
{
}"""

        # test_get(self, '/brapi/v1/studies/studies-search/?pageSize=2', expected)
        self.assertJSONEqual("{}", expected)

    # end def test_get_search


    def test_post_search(self):

        expected = """  
{
}"""

        params = {
            "observationUnitDbIds": ["2016-Maugio-34-575-abc-123"],
            "pageSize": 2
        }

        # test_post(self, '/brapi/v1/studies-search', params, expected)
        self.assertJSONEqual("{}", expected)

    # end def test_post_search


    def test_get_study_details(self):

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
                "endDate": "2014-01-01",
                "contacts": [
                    {
                        "orcid": "0000-0002-0607-8728",
                        "name": "A. Breeder",
                        "instituteName": "Plant Science Institute",
                        "contactDbId": "1",
                        "type": "Breeder",
                        "email": "a.breeder@brapi.org"
                    },
                    {
                        "orcid": "0000-0002-0607-8729",
                        "name": "B. Breeder",
                        "instituteName": "Plant Science Institute",
                        "contactDbId": "2",
                        "type": "Breeder",
                        "email": "b.breeder@brapi.org"
                    }
                ],
                "location": {
                    "latitude": -11.1275,
                    "locationDbId": "1",
                    "longitude": -75.356389,
                    "name": "Location 1",
                    "countryName": "Peru",
                    "instituteName": "Plant Science Institute",
                    "abbreviation": "L1",
                    "instituteAddress": "71 Pilgrim Avenue Chevy Chase MD 20815",
                    "type": "Storage location",
                    "additionalInfo": {
                        "altern": "SNPEDRO",
                        "local": "NaSARRI",
                        "cont": "Africa",
                        "creg": "SSA",
                        "adm3": "Coviriali",
                        "adm2": "Kassena-Nankana",
                        "adm1": "Serere",
                        "annualTotalPrecipitation": "6.4",
                        "annualMeanTemperature": "19.2"
                    },
                    "altitude": 828.0,
                    "countryCode": "PER"
                },
                "trialName": "Peru Yield Trial 1",
                "lastUpdate": {
                    "version": "1.1",
                    "timestamp": "2015-01-01T07:54:00Z"
                },
                "license": "https://creativecommons.org/licenses/by/4.0",
                "additionalInfo": {
                    "studyObjective": "Increase yield",
                    "publications": [
                        "pmid:24039865287545"
                    ]
                },
                "active": true,
                "studyDbId": "1001",
                "locationDbId": "1",
                "lastUpdateTimestamp": "2015-01-01T07:54:00Z",
                "studyName": "Study 1",
                "seasons": [
                    "2013 Spring",
                    "2011 Fall"
                ],
                "studyType": "Yield study",
                "studyDescription": "Field yield phenotyping study",
                "startDate": "2013-01-01",
                "dataLinks": [
                    {
                        "url": "http://data.inra.fr/archive/multi-spect-flowering.zip",
                        "name": "image-archive12.zip",
                        "type": "Image archive"
                    }
                ],
                "lastUpdateVersion": "1.1",
                "trialDbId": "101"
            }
        ]
    }
}"""

        test_get(self, '/brapi/v1/studies/1001/?pageSize=2', expected)

    # end def test_get_study_details


    def test_get_study_germplasm_details(self):

        expected = """  
{
}"""

        # test_get(self, '/brapi/v1/studies/1001/germplasm/?pageSize=2', expected)
        self.assertJSONEqual("{}", expected)

    # end def test_get_study_germplasm_details


    def test_get_study_observation_variable(self):

        expected = """  
{
}"""

        # test_get(self, '/brapi/v1/studies/1001/observationVariables/?pageSize=2', expected)
        self.assertJSONEqual("{}", expected)

    # end def test_get_study_observation_variable

# end class SampleTest
