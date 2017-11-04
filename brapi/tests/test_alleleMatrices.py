from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.markerprofiles import AlleleMSearchView
from brapi.models.markerprofile import AlleleMSearch


class AlleleMatrixSearchTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database
        AlleleMSearch.objects.create(data=['1', '1', 'A/B'])
        AlleleMSearch.objects.create(data=['1', '2', 'B'])
        AlleleMSearch.objects.create(data=['2', '2', 'A'])
        AlleleMSearch.objects.create(data=['2', '2', 'A/B'])

    # end def setUP


    def test_get_alleleMatrixSearch(self):

        view = AlleleMSearchView.as_view()

        factory = APIRequestFactory()
        request = factory.get('/brapi/b1/allelematrix-search')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content` without this.
        self.assertJSONEqual(response.content.decode('utf-8'), """
{
	"metadata": {
		"pagination": {
			"currentPage": 1,
			"pageTotal": 1,
			"totalCount": 4,
			"pageSize": 100
		},
		"status": [],
		"datafiles": []
	},
	"result": {
		"data": [
            [
                "1",
                "1",
                "A/B"
            ],
            [
                "1",
                "2",
                "B"
            ],
            [
                "2",
                "1",
                "A"
            ],
            [
                "2",
                "2",
                "A/B"
            ]
        ]
	}
}""")

    # end def test_get_alleleMatrixSearch

# end class AlleleMatrixSearchTest