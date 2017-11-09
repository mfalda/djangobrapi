from rest_framework.test import APITestCase

from brapi.aux_fun import test_get


class StudyTest(APITestCase):
    
    fixtures = ['study_obs_levels.json', 'study_seasons.json', 
                'study_types.json', 'study_obs_units.json',
                'study_plot_layouts.json']
    

    def test_get_obs_levels(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageSize": 100,
            "totalCount": 2,
            "pageTotal": 1
        },
        "datafiles": [],
        "status": []
    },
    "result": {
        "data": [
            "plant",
            "plot"
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/observationLevels/', expected)
        
    # end def test_get_obs_levels
    

    def test_get_seasons(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageSize": 2,
            "totalCount": 10,
            "pageTotal": 5
        },
        "datafiles": [],
        "status": []
    },
    "result": {
        "data": [
            {
                "seasonDbId": 1,
                "season": "spring",
                "year": 2011
            },
            {
                "seasonDbId": 2,
                "season": "summer",
                "year": 2011
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
                "name": "Yield Trial",
                "description": "Description for Trial study type"
            },
            {
                "name": "Genotype",
                "description": "Description for Genotyping study type"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/studyTypes/', expected)
       
    # end def test_get_types
    
    
    def test_get_obs_unit_details(self):

        expected = """    
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageSize": 100,
            "totalCount": 1,
            "pageTotal": 1
        },
        "datafiles": [],
        "status": []
    },
    "result": {
        "data": [
            {
                "studyDbId": 1,
                "observationDbId": 3383838,
                "observationUnitDbId": 11,
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "observationVariableDbId": 393939,
                "observationVariableName": "Yield",
                "observationTimestamp": "2015-11-05T14:12:56Z",
                "uploadedBy": "dbUserId",
                "operator": "Jane Doe",
                "germplasmDbId": 8383,
                "germplasmName": 143,
                "value": 5
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/studies/1/observationunits/', expected)
        
    # end def test_get_obs_unit_details 
        
    
    def test_get_plot_layout_details(self):

        expected = """  
    {
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageSize": 2,
            "totalCount": 6,
            "pageTotal": 3
        },
        "datafiles": [],
        "status": []
    },
    "result": {
        "data": [
            {
                "studyDbId": 1,
                "observationUnitDbId": 10001,
                "observationUnitName": "ZIPA_68_Ibadan_2014",
                "observationLevel": "plot",
                "replicate": 1,
                "germplasmDbId": 101,
                "germplasmName": "ZIPA_68",
                "blockNumber": 1,
                "X": 1,
                "Y": 1,
                "entryType": "test"
            },
            {
                "studyDbId": 1,
                "observationUnitDbId": 10002,
                "observationUnitName": "ZIPA_69_Ibadan_2014",
                "observationLevel": "plot",
                "replicate": 1,
                "germplasmDbId": 102,
                "germplasmName": "ZIPA_69",
                "blockNumber": 1,
                "X": 2,
                "Y": 1,
                "entryType": "test"
            }
        ]
    }
}"""
        
        test_get(self, '/brapi/v1/studies/1/layout/?pageSize=2', expected)
        
    # end def test_get_plot_layout_details 
    
# end class SampleTest
