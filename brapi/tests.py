from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from brapi.views import (CallsViewSet, CropsViewSet, LocationViewSet, ProgramViewSet, TraitViewSet, 
    SampleView, TrialViewSet, MarkerViewSet, AlleleMSearchView)
from brapi.models import Call, Crop, Location, Program, Trait, Sample, Study, Trial, Marker, AlleleMSearch


class CallsTest(APITestCase):

    def setUp(self):

        Call.objects.create(call='token', datatypes=['json', 'text'], methods=['POST', 'DELETE'])
        Call.objects.create(call='calls', datatypes=['json'], methods=['GET'])

    # end def setUP


    def test_get_calls(self):

        view = CallsViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/v1/calls/')

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
                    "call": "token",
                    "datatypes": [
                        "json",
                        "text"
                    ],
                    "methods": [
                        "POST",
                        "DELETE"
                    ]
                },
                {
                    "call": "calls",
                    "datatypes": [
                        "json"
                    ],
                    "methods": [
                        "GET"
                    ]
            }
        ]
    }
}""")

    # end def test_get_calls

# end class CallTest


class CropTest(APITestCase):

    def setUp(self):

        Crop.objects.create(data='cassava')
        Crop.objects.create(data='potato')
        Crop.objects.create(data='sweetpotato')
        Crop.objects.create(data='yam')

    # end def setUP


    def test_get_crops(self):

        view = CropsViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/v1/crops/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content.decode('utf-8')` without this.
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
            "cassava",
            "potato",
            "sweetpotato",
            "yam"
        ]
    }
}""")

    # end def test_get_crops

# end class CropTest


class LocationTest(APITestCase):
 
    def setUp(self):

        Location.objects.create(locationDbId='1',
                     locationType='Storage location',
                     name='Experimental station San Ramon (CIP)',
                     abbreviation='CIPSRM-1',
                     countryCode='PER',
                     countryName='Peru',
                     latitude='-11.1275',
                     longitude='-75.356389',
                     altitude='828',
                     instituteName='INRA - GDEC',
                     instituteAdress='route foo, Clermont Ferrand, France')
        Location.objects.create(locationDbId='2',
                     locationType='Breeding location',
                     name='San Ramon',
                     abbreviation='CIPSRM-2',
                     countryCode='PER',
                     countryName='Peru',
                     latitude='-11.16116',
                     longitude='-75.34171',
                     altitude='964',
                     instituteName='INRA - GDEC',
                     instituteAdress='route foo, Clermont Ferrand, France')

    # end def setUP


    def test_get_locations(self):

        view = LocationViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/v1/locations/')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render()
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
                "locationDbId": "1",
                "locationType": "Storage location",
                "name": "Experimental station San Ramon (CIP)",
                "abbreviation": "CIPSRM-1",
                "countryCode": "PER",
                "countryName": "Peru",
                "latitude": -11.1275,
                "longitude": -75.356389,
                "altitude": "828",
                "instituteName": "INRA - GDEC",
                "instituteAdress": "route foo, Clermont Ferrand, France"
            },
            {
                "locationDbId": "2",
                "locationType": "Breeding location",
                "name": "San Ramon",
                "abbreviation": "CIPSRM-2",
                "countryCode": "PER",
                "countryName": "Peru",
                "latitude": -11.16116,
                "longitude": -75.34171,
                "altitude": "964",
                "instituteName": "INRA - GDEC",
                "instituteAdress": "route foo, Clermont Ferrand, France"
            }
        ]
    }
}""")

    # end def test_get_locations

# end class LocationTest


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


class TraitTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database        
        Trait.objects.create(traitDbId='1', traitId='CO_334:0100620', name='Carotenoid content', description='Cassava storage root pulp carotenoid content', observationVariables=['CO_334:0100621', 'CO_334:0100623', 'CO_334:0100623'])
        Trait.objects.create(traitDbId='2', traitId='CO_334:0100621', name='Plant height', description='Plant height', observationVariables=['CO_334:0200001'])

    # end def setUP


    def test_get_traits(self):

        view = TraitViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/b1/Traits/')

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
                "traitDbId": 1,
                "traitId": "CO_334:0100620",
                "name": "Carotenoid content",
                "description": "Cassava storage root pulp carotenoid content",
                "observationVariables": [
                    "CO_334:0100621",
                    "CO_334:0100623",
                    "CO_334:0100623"
                ],
                "defaultValue": null
            },
            {
                "traitDbId": 2,
                "traitId": "CO_334:0100621",
                "name": "Plant height",
                "description": "Plant height",
                "observationVariables": [
                    "CO_334:0200001"
                ],
                "defaultValue": null
            }
        ]
    }
}""")

    # end def test_get_traits

# end class TraitTest


class SampleTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database
        Sample.objects.create(studyDbId='StudyId-123', locationDbId='LocationId-123', plotId='PlotId-123', 
            plantId='PlantID-123', sampleId='Unique-Plant-SampleID', takenBy='Mr. Technician', 
            sampleTimestamp='2016-07-27T14:43:22+0100', sampleType='TypeOfSample', tissueType='TypeOfTissue', 
            notes='Cut from infected leaf', studyName='Yield Trial A', season='Summer', locationName='Kenya', 
            entryNumber=11, plotNumber=1, germplasmDbId=15, plantingTimestamp='2016-01-01T23:22:21+0100', 
            harvestTimestamp='2016-06-30T23:33:23+0100')

    # end def setUP


    def test_get_samples(self):

        view = SampleView.as_view()

        factory = APIRequestFactory()
        request = factory.get('/brapi/b1/samples/Unique-Plant-SampleID')

        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.render() # Cannot access `response.content` without this.
        self.assertJSONEqual(response.content.decode('utf-8'), """
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
                "studyDbId": "StudyId-123",
                "locationDbId": "LocationId-123",
                "plotId": "PlotId-123",
                "plantId": "PlantID-123",
                "sampleId": "Unique-Plant-SampleID",
                "takenBy": "Mr. Technician",
                "sampleTimestamp": "2016-07-27T13:43:22Z",
                "sampleType": "TypeOfSample",
                "tissueType": "TypeOfTissue",
                "notes": "Cut from infected leaf",
                "studyName": "Yield Trial A",
                "season": "Summer",
                "locationName": "Kenya",
                "entryNumber": 11,
                "plotNumber": 1,
                "germplasmDbId": 15,
                "plantingTimestamp": "2016-01-01T22:22:21Z",
                "harvestTimestamp": "2016-06-30T22:33:23Z"
            }
        ]
    }
}""")

    # end def test_get_samples

# end class SampleTest


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


class MarkerTest(APITestCase):
    
    def setUp(self):

        # populate the mockup database
        Marker.objects.create(markerDbId='1', defaultDisplayName='a_01_10001', type='SNP', 
		    synonyms=['i_01_10001', 'popA_10001'], refAlt=['A', 'T'], analysisMethods=['illumina'])
        Marker.objects.create(markerDbId='2', defaultDisplayName='A_01_10002', type='SNP', 
		    synonyms=['i_01_10001', 'popA_10002'], refAlt=['G', 'C'], analysisMethods=['illumina'])


    # end def setUP


    def test_get_markers(self):

        view = MarkerViewSet.as_view({'get': 'list'})

        factory = APIRequestFactory()
        request = factory.get('/brapi/b1/markers/')

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
                "markerDbId": 1,
                "defaultDisplayName": "a_01_10001",
                "type": "SNP",
                "synonyms": [
                    "i_01_10001",
                    "popA_10001"
                ],
                "refAlt": [
                    "A",
                    "T"
                ],
                "analysisMethods": [
                    "illumina"
                ]
            },
            {
                "markerDbId": 2,
                "defaultDisplayName": "A_01_10002",
                "type": "SNP",
                "synonyms": [
                    "i_01_10001",
                    "popA_10002"
                ],
                "refAlt": [
                    "G",
                    "C"
                ],
                "analysisMethods": [
                    "illumina"
                ]
            }
		]
	}
}""")

    # end def test_get_markers

# end class MarkerTest


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