from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase

from brapi.views.programs import ProgramViewSet
from brapi.models.program import Program


class ProgramTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database
        Program.objects.create(programDbId="1", name="CIPHQ", abbreviation="CIPHQ", objective="Global Population Improvement", leadPerson="G. Leader")
        Program.objects.create(programDbId="2", name="Ghana", abbreviation="GHA", objective="OFSP", leadPerson="M. Breeder")

    # end def setUP


    def test_get_programs(self):

        view = ProgramViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/v1/programs/')

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
                "programDbId": 1,
                "name": "CIPHQ",
                "abbreviation": "CIPHQ",
                "objective": "Global Population Improvement",
                "leadPerson": "G. Leader"
            },
            {
                "programDbId": 2,
                "name": "Ghana",
                "abbreviation": "GHA",
                "objective": "OFSP",
                "leadPerson": "M. Breeder"
            }
        ]
    }
}""")

    # end def test_get_programs

# end class ProgramTest
