from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.trials import TrialViewSet
from brapi.models.study import Study, Trial


class TrialTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database

        t1 = Trial.objects.create(trialDbId='1', trialName='Peru Yield Trial', programDbId='1', name='CIPHQ', 
            startDate='2013-01-01', endDate='2013-07-05', active='False')

        t2 = Trial.objects.create(trialDbId='2', trialName='Peru Genotype Trial', programDbId='1', name='CIPHQ', 
            startDate='2014-06-01', endDate='2015-01-15', active='False')

        Study.objects.create(studyDbId='1', studyName='Peru Yield Trial', locationName='Experimental station San Ramon (CIP)', trialDbId=t1)
        Study.objects.create(studyDbId='2', studyName='Peru Genotype Trial', locationName='San Ramon', trialDbId=t2)

    # end def setUP


    def test_get_trials(self):

        view = TrialViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/b1/trials/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content` without this.
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
                "trialDbId": 1,
                "trialName": "Peru Yield Trial",
                "programDbId": 1,
                "name": "CIPHQ",
                "startDate": "2013-01-01",
                "endDate": "2013-07-05",
                "active": false,
                "studies": [
                    {
                        "studyDbId": 1,
                        "studyName": "Peru Yield Trial",
                        "locationName": "Experimental station San Ramon (CIP)"
                    }
                ]
            },
            {
                "trialDbId": 2,
                "trialName": "Peru Genotype Trial",
                "programDbId": 1,
                "name": "CIPHQ",
                "startDate": "2014-06-01",
                "endDate": "2015-01-15",
                "active": false,
                "studies": [
                    {
                        "studyDbId": 2,
                        "studyName": "Peru Genotype Trial",
                        "locationName": "San Ramon"
                    }
                ]
            }
        ]
    }
}""")

    # end def test_get_trials

# end class TrialTest
