from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.conf.urls import handler400, handler403, handler404, handler500

from brapi.views.authentication import exchange_token
from brapi.views import errors
from brapi.views.calls import CallsViewSet
from brapi.views.locations import LocationView, LocationDetailsView
from brapi.views.crops import CropsViewSet
from brapi.views.programs import ProgramViewSet, ProgramSearchView
from brapi.views.maps import MapViewSet, MapLinkageView, MapLinkageViewPositions
from brapi.views.markers import MarkerView, MarkerDetailsView
from brapi.views.traits import TraitView, TraitDetailsView
from brapi.views.germplasm_attributes import (GAListViewSet, GAAttrAvailViewSet, 
                                              GermplasmAttrView)
from brapi.views.germplasm import (GermplasmView, GPPedigreeView, 
                                   GermplasmSearchView)
from brapi.views.trials import TrialView, TrialDetailsView
from brapi.views.samples import SampleView
from brapi.views.phenotypes import PhenotypeSearchView
from brapi.views.markerprofiles import (AlleleMatrixViewSet, AlleleMSearchView, 
                                        MarkerProfilesView, MarkerProfilesDataView,
                                        GPMarkerPView)
from brapi.views.obs_variables import (DatatypesViewSet, OntologiesViewSet,
                                       ObsVariablesListView, ObsVariablesView, 
                                       VSearchView)
from brapi.views.studies import (StudyPlotView, SSearchView, 
                                 StudyObsUnitsDetailsView, StudyDetailsView,
                                 StudyGermplasmDetailsView, StudyObsUnitsTableView, 
                                 StudyObsVarsView, StudySeasonsViewSet, 
                                 StudyTypesViewSet, StudyObsLevelsViewSet) 
#StudyObsUnitsView


handler400 = errors.error400
handler404 = errors.error404

# since we're using viewsets and routers, we can simply use the automatic schema generation.
schema_view = get_schema_view(title='BrAPI')

# bind our ViewSet classes into a set of concrete views (the http methods to the required action for each view)
calls = CallsViewSet.as_view({
    'get': 'list',
})

# Because we're using ViewSet classes rather than View classes,
# the conventions for wiring up resources into views and urls can be handled automatically
# using a Router class.
# Create a router and register our viewsets with it (the URL prefix and the ViewSet)
router = DefaultRouter()

router.register(r'brapi/v1/crops', CropsViewSet, 'crops')
router.register(r'brapi/v1/calls', CallsViewSet, 'calls')
router.register(r'brapi/v1/programs', ProgramViewSet, 'programs')
router.register(r'brapi/v1/maps', MapViewSet, 'maps')
router.register(r'brapi/v1/attributes/categories', GAListViewSet, 'GA_list')
router.register(r'brapi/v1/attributes', GAAttrAvailViewSet, 'GA_attr_avail')
router.register(r'brapi/v1/variables/datatypes', DatatypesViewSet, 'datatypes')
router.register(r'brapi/v1/ontologies', OntologiesViewSet, 'ontologies')
router.register(r'brapi/v1/seasons', StudySeasonsViewSet, 'study_seasons')
router.register(r'brapi/v1/observationLevels', StudyObsLevelsViewSet, 'study_obs_levels')
router.register(r'brapi/v1/studyTypes', StudyTypesViewSet, 'study_types')
router.register(r'brapi/v1/allelematrices', AlleleMatrixViewSet, 'allele_matrix')

# The API URLs are now determined automatically by the router
# Additionally, we include the login URLs for the browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    # cannot use ViewSets because the detail view is not standard
    url(r'brapi/v1/maps/(?P<mapDbId>[0-9]+)/positions/?$', MapLinkageView.as_view(), name='map_positions'),
    url(r'brapi/v1/maps/(?P<mapDbId>[0-9]+)/positions/(?P<linkageGroupId>[0-9]+)/?$', MapLinkageViewPositions.as_view()),

    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[0-9]+)/attributes/?$', GermplasmAttrView.as_view()),

    url(r'brapi/v1/studies/(?P<studyDbId>[0-9]+)/germplasm/?$', GermplasmView.as_view()),

    url(r'brapi/v1/locations/(?P<locationDbId>[0-9]+)/?$', LocationDetailsView.as_view()),
    url(r'brapi/v1/locations/?$', LocationView.as_view()),
    
    url(r'brapi/v1/germplasm/(?P<id>[0-9]+)/markerprofiles/?$', GPMarkerPView.as_view()),
    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[0-9]+)/pedigree/?$', GPPedigreeView.as_view()),
    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[0-9]+)/?$', GermplasmView.as_view()),
    url(r'brapi/v1/germplasm-search/?$', GermplasmSearchView.as_view()),

    # written as a view to block 'brapi/v1/samples'
    url(r'brapi/v1/samples/(?P<sampleId>.+)/?$', SampleView.as_view()),

    url(r'brapi/v1/phenotypes-search/?$', PhenotypeSearchView.as_view()),

    url(r'brapi/v1/programs-search/?$', ProgramSearchView.as_view()), 
    
    url(r'brapi/v1/studies/(?P<studyDbId>[0-9]+)/layout/?$', StudyPlotView.as_view()),

    url(r'brapi/v1/allelematrix-search/?', AlleleMSearchView.as_view()),

    url(r'brapi/v1/markers/(?P<markerDbId>[0-9]+)/?$', MarkerDetailsView.as_view()),
    url(r'brapi/v1/markers/?$', MarkerView.as_view()),
    
    url(r'brapi/v1/markerprofiles/(?P<markerprofileDbId>[0-9]+)/?$', MarkerProfilesDataView.as_view()),
    url(r'brapi/v1/markerprofiles/?$', MarkerProfilesView.as_view()),

    url(r'brapi/v1/trials/(?P<trialDbId>[0-9]+)/?$', TrialDetailsView.as_view()),
    url(r'brapi/v1/trials', TrialView.as_view()),
    
    url(r'brapi/v1/variables/(?P<observationVariableDbId>.+)/$', ObsVariablesView.as_view()),
    url(r'brapi/v1/variables/?$', ObsVariablesListView.as_view()),
    url(r'brapi/v1/variables-search/?$', VSearchView.as_view()),

    url(r'brapi/v1/traits/(?P<traitDbId>[0-9]+)/?$', TraitDetailsView.as_view()),
    url(r'brapi/v1/traits/?', TraitView.as_view()),
    
    url(r'brapi/v1/studies/studies-search/?$', SSearchView.as_view()),    
    #url(r'brapi/v1/studies/(?P<studyDbId>.+)/observations$', StudyObsUnitsView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observationunits/?$', StudyObsUnitsDetailsView.as_view()),    
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/germplasm/?$', StudyGermplasmDetailsView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/table/?$', StudyObsUnitsTableView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observationVariables/?$', StudyObsVarsView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/?$', StudyDetailsView.as_view())
]

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^brapi/v1/token/(?P<backend>[^/]+)/', exchange_token),
    url('', include('social_django.urls', namespace='social'))
]