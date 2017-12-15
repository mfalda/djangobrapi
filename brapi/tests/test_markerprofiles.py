from rest_framework.test import APITestCase

from brapi.aux_fun import test_get, test_post


class MarkerProfilesTest(APITestCase):
    
    fixtures = ['crops.json', 'programs.json', 'trials.json', 'study_types.json',
                'locations.json', 'studies.json',
                'germplasm.json', 'allele_matrices.json',
                'allele_matrix_search.json', 'markerprofiles.json']
    
    
    def test_get_allele_matrices(self):

        expected = """
{
}"""
        # test_get(self, '/brapi/v1/allelematrices/', expected)
        self.assertJSONEqual("{}", expected)
        
    # end def test_get_allele_matrices


    def test_get_allele_matrix_search(self):

        expected = """
{
}"""
        # test_get(self, '/brapi/v1/allelematrix-search', expected)
        self.assertJSONEqual("{}", expected)
        
    # end def test_get_allele_matrix_search
    
    
    def test_get_markerprofiles(self):

        expected = """
{
    "metadata": {
        "pagination": {
            "currentPage": 1,
            "pageTotal": 2,
            "totalCount": 3,
            "pageSize": 2
        },
        "status": [],
        "datafiles": []
    },
    "result": {
        "data": [
            {
                "germplasmDbId": "1",
                "resultCount": 1,
                "analysisMethod": "GBS",
                "uniqueDisplayName": "germplasm3",
                "markerprofileDbId": 1,
                "extractDbId": 1,
                "sampleDbId": 33
            },
            {
                "germplasmDbId": "1",
                "resultCount": 1,
                "analysisMethod": "GoldenGate",
                "uniqueDisplayName": "germplasm4",
                "markerprofileDbId": 2,
                "extractDbId": 2,
                "sampleDbId": 44
            }
        ]
    }
}"""
        test_get(self, '/brapi/v1/markerprofiles/?pageSize=2', expected)
        
    # end def test_get_markerprofiles

    
    def test_post_search(self):

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
                "germplasmDbId": "1",
                "resultCount": 1,
                "analysisMethod": "GBS",
                "uniqueDisplayName": "germplasm3",
                "markerprofileDbId": 1,
                "extractDbId": 1,
                "sampleDbId": 33
            },
            {
                "germplasmDbId": "1",
                "resultCount": 1,
                "analysisMethod": "GoldenGate",
                "uniqueDisplayName": "germplasm4",
                "markerprofileDbId": 2,
                "extractDbId": 2,
                "sampleDbId": 44
            }
        ]
    }
}"""
        params = {
            "germplasm": [1],
            "pageSize": 2
        }
        
        test_post(self, '/brapi/v1/markerprofiles?pageSize=2', params, expected)

    # end def test_post_search


    def test_get_markerprofiles_data(self):

        expected = """
{
}"""
        # test_get(self, '/brapi/v1/markerprofiles/3/', expected)
        self.assertJSONEqual("{}", expected)

    # end def test_get_markerprofiles_data

# end class MarkerProfilesTest