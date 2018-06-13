from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
import oauth2_provider.views as oauth2_views
from django.conf import settings

from brapi.views import index
from brapi.views import errors
from brapi.views.calls import CallsView
from brapi.views.locations import LocationView, LocationDetailsView
from brapi.views.crops import CropsView
from brapi.views.programs import ProgramView, ProgramSearchView
from brapi.views.maps import MapView, MapDetailView, MapLinkageView, MapLinkageViewPositions
from brapi.views.markers import MarkerView, MarkerDetailsView
from brapi.views.traits import TraitView, TraitDetailsView
from brapi.views.germplasm_attributes import (GermplasmAttributesListView, GermplasmAttributesAvailailableView,
                                                GermplasmAttributeView)
from brapi.views.germplasm import (GermplasmPedigreeView, GermplasmView, GermplasmSearchView)
from brapi.views.trials import TrialView, TrialDetailsView
from brapi.views.samples import SampleView, SampleSearchView
from brapi.views.phenotypes import PhenotypeSearchView
from brapi.views.markerprofiles import (AlleleMatrixView, AlleleMatrixSearchView,
                                        MarkerprofileView, MarkerprofileDataView,
                                        GermplasmMarkeprofileView)
from brapi.views.observation_variables import (ObservationVariableSearchView, ObservationVariablesListView,
                                               ObservationVariableView, OntologyView,
                                               ObservationVariableDatatypeView)
from brapi.views.studies import (StudySeasonView, StudySearchView, StudyTypeView,
                                 StudyObservationLevelView, StudyDetailView, StudyPlotLayoutView,
                                 StudyObservationVariableView, StudyGermplasmDetailsView,
                                 StudyObservationUnitDetailsView, StudyObservationUnitByObservationVariableView)


handler400 = errors.error400
handler404 = errors.error404

# since we're using viewsets and routers, we can simply use the automatic schema generation.
schema_view = get_schema_view(title='BrAPI')

# The API URLs are now determined automatically by the router
# Additionally, we include the login URLs for the browsable API
urlpatterns = [
#    url(r'^', include(router.urls)),

    url(r'brapi/v1/?$', index.index, name='index'),

    url(r'brapi/v1/crops/?', CropsView.as_view()),

    url(r'brapi/v1/calls/?', CallsView.as_view()),

    url(r'brapi/v1/maps/?$', MapView.as_view()),
    url(r'brapi/v1/maps/(?P<mapDbId>[^/]+)/?$', MapDetailView.as_view()),
    url(r'brapi/v1/maps/(?P<mapDbId>[^/]+)/positions/?$', MapLinkageView.as_view(), name='map_positions'),
    url(r'brapi/v1/maps/(?P<mapDbId>[^/]+)/positions/(?P<linkageGroupId>[^/]+)/?$', MapLinkageViewPositions.as_view()),

    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[^/]+)/attributes/?$', GermplasmAttributeView.as_view()),
    url(r'brapi/v1/attributes/categories/?', GermplasmAttributesListView.as_view()),
    url(r'brapi/v1/attributes/?', GermplasmAttributesAvailailableView.as_view()),

    url(r'brapi/v1/locations/(?P<locationDbId>[^/]+)/?$', LocationDetailsView.as_view()),
    url(r'brapi/v1/locations/?$', LocationView.as_view()),
    
    url(r'brapi/v1/germplasm/(?P<id>[^/]+)/markerprofiles/?$', GermplasmMarkeprofileView.as_view()),
    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[^/]+)/pedigree/?$', GermplasmPedigreeView.as_view()),
    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[^/]+)/?$', GermplasmView.as_view()),
    url(r'brapi/v1/germplasm-search/?$', GermplasmSearchView.as_view()),

    # written as a view to block 'brapi/v1/samples'
    url(r'brapi/v1/samples/(?P<sampleId>[^/]+)/?$', SampleView.as_view()),
    url(r'brapi/v1/samples-search/?$', SampleSearchView.as_view()),

    url(r'brapi/v1/phenotypes-search/?$', PhenotypeSearchView.as_view()),

    url(r'brapi/v1/programs-search/?$', ProgramSearchView.as_view()),
    url(r'brapi/v1/programs/?', ProgramView.as_view()),

    url(r'brapi/v1/allelematrices/?', AlleleMatrixView.as_view()),
    url(r'brapi/v1/allelematrix-search/?', AlleleMatrixSearchView.as_view()),

    url(r'brapi/v1/markers/(?P<markerDbId>[^/]+)/?$', MarkerDetailsView.as_view()),
    url(r'brapi/v1/markers/?$', MarkerView.as_view()),
    
    url(r'brapi/v1/markerprofiles/(?P<markerprofileDbId>[^/]+)/?$', MarkerprofileDataView.as_view()),
    url(r'brapi/v1/markerprofiles/?$', MarkerprofileView.as_view()),

    url(r'brapi/v1/trials/(?P<trialDbId>[^/]+)/?$', TrialDetailsView.as_view()),
    url(r'brapi/v1/trials', TrialView.as_view()),

    url(r'brapi/v1/ontologies/?$', OntologyView.as_view()),
    url(r'brapi/v1/variables/datatypes/?$', ObservationVariableDatatypeView.as_view()),
    url(r'brapi/v1/variables/(?P<observationVariableDbId>[^/]+)/?$', ObservationVariableView.as_view()),
    url(r'brapi/v1/variables/?$', ObservationVariablesListView.as_view()),
    url(r'brapi/v1/variables-search/?$', ObservationVariableSearchView.as_view()),

    url(r'brapi/v1/traits/(?P<traitDbId>[^/]+)/?$', TraitDetailsView.as_view()),
    url(r'brapi/v1/traits/?', TraitView.as_view()),

    url(r'brapi/v1/seasons/?', StudySeasonView.as_view()),
    url(r'brapi/v1/observationlevels/?', StudyObservationLevelView.as_view()),
    url(r'brapi/v1/studytypes/?', StudyTypeView.as_view()),
    url(r'brapi/v1/studies-search/?$', StudySearchView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observations/?$', StudyObservationUnitByObservationVariableView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observationunits/?$', StudyObservationUnitDetailsView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/germplasm/?$', StudyGermplasmDetailsView.as_view()),
#    url(r'brapi/v1/studies/(?P<studyDbId>.+)/table/?$', StudyObsUnitsTableView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observationvariables/?$', StudyObservationVariableView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>[^/]+)/?$', StudyDetailView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>[^/]+)/layout/?$', StudyPlotLayoutView.as_view())
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
