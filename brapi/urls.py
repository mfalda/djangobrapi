from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.conf.urls import handler400, handler403, handler404, handler500
import oauth2_provider.views as oauth2_views
from django.conf import settings

from brapi.views import errors
from brapi.views.calls import CallsView
from brapi.views.locations import LocationView, LocationDetailsView
from brapi.views.crops import CropsViewSet
from brapi.views.programs import ProgramViewSet, ProgramSearchView
from brapi.views.maps import MapView, MapDetailView, MapLinkageView, MapLinkageViewPositions
from brapi.views.markers import MarkerView, MarkerDetailsView
from brapi.views.traits import TraitView, TraitDetailsView
from brapi.views.germplasm_attributes import (GermplasmAttributesListViewSet, GermplasmAttributesAvailailableViewSet,
                                                GermplasmAttributeView)
from brapi.views.germplasm import (GermplasmView, GermplasmPedigreeView,
                                   GermplasmSearchView)
from brapi.views.germplasm import GermplasmView, GermplasmSearchView
from brapi.views.trials import TrialView, TrialDetailsView
from brapi.views.samples import SampleView
from brapi.views.phenotypes import PhenotypeSearchView
from brapi.views.markerprofiles import (AlleleMatrixViewSet, AlleleMatrixSearchView,
                                        MarkerProfilesView, MarkerProfilesDataView,
                                        GermplasmMarkeprofileView)
#from brapi.views.obs_variables import VSearchView
from brapi.views.obs_variables import (ObservationVariablesListView, ObservationVariableView, OntologiesViewSet,
                                       ObservationVariableDatatypeViewSet)
#from brapi.views.studies import (StudyPlotView, StudyObsUnitsView,
#                                 StudyObsUnitsDetailsView, StudyDetailsView,
#                                 StudyGermplasmDetailsView, StudyObsUnitsTableView,
#                                 StudyObsVarsView, StudySeasonViewSet,
#                                 StudyTypesViewSet, StudyObsLevelsViewSet)
from brapi.views.studies import StudySeasonViewSet, StudySearchView, StudyTypeViewSet, StudyObservationLevelViewSet


handler400 = errors.error400
handler404 = errors.error404

# since we're using viewsets and routers, we can simply use the automatic schema generation.
schema_view = get_schema_view(title='BrAPI')

# Because we're using ViewSet classes rather than View classes,
# the conventions for wiring up resources into views and urls can be handled automatically
# using a Router class.
# Create a router and register our viewsets with it (the URL prefix and the ViewSet)
router = DefaultRouter()

router.register(r'brapi/v1/crops', CropsViewSet, 'crops')
router.register(r'brapi/v1/programs', ProgramViewSet, 'programs')
router.register(r'brapi/v1/attributes/categories', GermplasmAttributesListViewSet, 'GA_list')
router.register(r'brapi/v1/attributes', GermplasmAttributesAvailailableViewSet, 'GA_attr_avail')
router.register(r'brapi/v1/variables/datatypes', ObservationVariableDatatypeViewSet, 'datatypes')
router.register(r'brapi/v1/ontologies', OntologiesViewSet, 'ontologies')
router.register(r'brapi/v1/seasons', StudySeasonViewSet, 'study_seasons')
router.register(r'brapi/v1/observationLevels', StudyObservationLevelViewSet, 'study_obs_levels')
router.register(r'brapi/v1/studyTypes', StudyTypeViewSet, 'study_types')
router.register(r'brapi/v1/allelematrices', AlleleMatrixViewSet, 'allele_matrix')

# The API URLs are now determined automatically by the router
# Additionally, we include the login URLs for the browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'brapi/v1/calls', CallsView.as_view()),

    url(r'brapi/v1/maps/?$', MapView.as_view()),
    url(r'brapi/v1/maps/(?P<mapDbId>[0-9]+)/?$', MapDetailView.as_view()),
    url(r'brapi/v1/maps/(?P<mapDbId>[0-9]+)/positions/?$', MapLinkageView.as_view(), name='map_positions'),
    url(r'brapi/v1/maps/(?P<mapDbId>[0-9]+)/positions/(?P<linkageGroupId>[0-9]+)/?$', MapLinkageViewPositions.as_view()),

    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[0-9]+)/attributes/?$', GermplasmAttributeView.as_view()),

#    url(r'brapi/v1/studies/(?P<studyDbId>[0-9]+)/germplasm/?$', GermplasmView.as_view()),

    url(r'brapi/v1/locations/(?P<locationDbId>[0-9]+)/?$', LocationDetailsView.as_view()),
    url(r'brapi/v1/locations/?$', LocationView.as_view()),
    
    url(r'brapi/v1/germplasm/(?P<id>[0-9]+)/markerprofiles/?$', GermplasmMarkeprofileView.as_view()),
    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[0-9]+)/pedigree/?$', GermplasmPedigreeView.as_view()),
    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[0-9]+)/?$', GermplasmView.as_view()),
    url(r'brapi/v1/germplasm-search/?$', GermplasmSearchView.as_view()),

    # written as a view to block 'brapi/v1/samples'
    url(r'brapi/v1/samples/(?P<sampleId>.+)/?$', SampleView.as_view()),

    url(r'brapi/v1/phenotypes-search/?$', PhenotypeSearchView.as_view()),

    url(r'brapi/v1/programs-search/?$', ProgramSearchView.as_view()), 
    
#    url(r'brapi/v1/studies/(?P<studyDbId>[0-9]+)/layout/?$', StudyPlotView.as_view()),

    url(r'brapi/v1/allelematrix-search/?', AlleleMatrixSearchView.as_view()),

    url(r'brapi/v1/markers/(?P<markerDbId>[0-9]+)/?$', MarkerDetailsView.as_view()),
    url(r'brapi/v1/markers/?$', MarkerView.as_view()),
    
    url(r'brapi/v1/markerprofiles/(?P<markerprofileDbId>[0-9]+)/?$', MarkerProfilesDataView.as_view()),
    url(r'brapi/v1/markerprofiles/?$', MarkerProfilesView.as_view()),

    url(r'brapi/v1/trials/(?P<trialDbId>[0-9]+)/?$', TrialDetailsView.as_view()),
    url(r'brapi/v1/trials', TrialView.as_view()),
    
    url(r'brapi/v1/variables/(?P<observationVariableDbId>.+)/$', ObservationVariableView.as_view()),
    url(r'brapi/v1/variables/?$', ObservationVariablesListView.as_view()),
#    url(r'brapi/v1/variables-search/?$', VSearchView.as_view()),

    url(r'brapi/v1/traits/(?P<traitDbId>[0-9]+)/?$', TraitDetailsView.as_view()),
    url(r'brapi/v1/traits/?', TraitView.as_view()),
    
    url(r'brapi/v1/studies-search/?$', StudySearchView.as_view()),
#    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observations$', StudyObsUnitsView.as_view()),
#    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observationunits/?$', StudyObsUnitsDetailsView.as_view()),
#    url(r'brapi/v1/studies/(?P<studyDbId>.+)/germplasm/?$', StudyGermplasmDetailsView.as_view()),
#    url(r'brapi/v1/studies/(?P<studyDbId>.+)/table/?$', StudyObsUnitsTableView.as_view()),
#    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observationVariables/?$', StudyObsVarsView.as_view()),
#    url(r'brapi/v1/studies/(?P<studyDbId>.+)/?$', StudyDetailsView.as_view())
]

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    url(r'brapi/v1/authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r'brapi/v1/token/$', oauth2_views.TokenView.as_view(), name="token"),
    url(r'brapi/v1/revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        url(r'brapi/v1/applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        url(r'brapi/v1/applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        url(r'brapi/v1/applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        url(r'brapi/v1/applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        url(r'brapi/v1/applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        url(r'brapi/v1/authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        url(r'brapi/v1/authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]

urlpatterns = [
    # OAuth 2 endpoints:
    url(r'', include(oauth2_endpoint_views, namespace="oauth2_provider")),
    url(r'', include(urlpatterns)),    
]
