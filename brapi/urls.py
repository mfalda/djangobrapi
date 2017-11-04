from django.conf.urls import url, include
from brapi import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from brapi.views import (CallsViewSet, LocationViewSet, CropsViewSet, DatatypesViewSet,
    MapViewSet, MapLinkageView, MapLinkageViewPositions, MarkerViewSet, TraitViewSet,
    GAListViewSet, GAAttrAvailViewSet, GermplasmAttrView, GermplasmView, GPPedigreeView,
    GPMarkerPView, GermplasmSearchView, TrialViewSet, SampleView, PhenotypeSearchView,
    OntologiesViewSet, StudySeasonsViewSet, StudyTypesViewSet, StudyObsLevelsViewSet,
    StudyPlotView, AlleleMatrixViewSet, AlleleMSearchView, MarkerProfilesDataView, 
    MarkerProfilesDataView, ObsVariablesListView, ObsVariablesView, VSearchView,
    StudyObsUnitsView, SSearchView, StudyObsUnitsDetailsView, StudyDetailsView,
    StudyGermplasmDetailsView, StudyObsUnitsTableView, StudyObsVarsView)


# since we're using viewsets and routers, we can simply use the automatic schema generation.
schema_view = get_schema_view(title='BrAPI')

# bind our ViewSet classes into a set of concrete views (the http methods to the required action for each view)
calls = CallsViewSet.as_view({
    'get': 'list',
})
locations = LocationViewSet.as_view({
    'get': 'list',
})

# Because we're using ViewSet classes rather than View classes,
# the conventions for wiring up resources into views and urls can be handled automatically
# using a Router class.
# Create a router and register our viewsets with it (the URL prefix and the ViewSet)
router = DefaultRouter()

router.register(r'brapi/v1/crops', views.CropsViewSet, 'crops')
router.register(r'brapi/v1/calls', views.CallsViewSet, 'calls')
router.register(r'brapi/v1/locations', views.LocationViewSet, 'locations')
router.register(r'brapi/v1/programs', views.ProgramViewSet, 'programs')
router.register(r'brapi/v1/maps', views.MapViewSet, 'maps')
router.register(r'brapi/v1/markers', views.MarkerViewSet, 'markers')
router.register(r'brapi/v1/traits', views.TraitViewSet, 'traits')
router.register(r'brapi/v1/attributes/categories', views.GAListViewSet, 'GA_list')
router.register(r'brapi/v1/attributes', views.GAAttrAvailViewSet, 'GA_attr_avail')
router.register(r'brapi/v1/trials', views.TrialViewSet, 'trials')
router.register(r'brapi/v1/variables/datatypes', views.DatatypesViewSet, 'datatypes')
router.register(r'brapi/v1/ontologies', views.OntologiesViewSet, 'ontologies')
router.register(r'brapi/v1/seasons', views.StudySeasonsViewSet, 'study_seasons')
router.register(r'brapi/v1/observationLevels', views.StudyObsLevelsViewSet, 'study_obs_levels')
router.register(r'brapi/v1/studyTypes', views.StudyTypesViewSet, 'study_types')
router.register(r'brapi/v1/allelematrices', views.AlleleMatrixViewSet, 'allele_matrix')

# The API URLs are now determined automatically by the router
# Additionally, we include the login URLs for the browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    # cannot use ViewSets because the detail view is not standard
    url(r'brapi/v1/maps/(?P<mapDbId>[0-9]+)/positions$', views.MapLinkageView.as_view()),
    url(r'brapi/v1/maps/(?P<mapDbId>[0-9]+)/positions/(?P<linkageGroupId>[0-9]+)$', views.MapLinkageViewPositions.as_view()),

    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[0-9]+)/attributes$', views.GermplasmAttrView.as_view()),

    url(r'brapi/v1/studies/(?P<studyDbId>[0-9]+)/germplasm$', views.GermplasmView.as_view()),

    url(r'brapi/v1/germplasm/(?P<id>[0-9]+)/markerprofiles$', views.GPMarkerPView.as_view()),
    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[0-9]+)/pedigree$', views.GPPedigreeView.as_view()),
    url(r'brapi/v1/germplasm/(?P<germplasmDbId>[0-9]+)$', views.GermplasmView.as_view()),
    url(r'brapi/v1/germplasm-search$', views.GermplasmSearchView.as_view()),

    # written as a view to block 'brapi/v1/samples'
    url(r'brapi/v1/samples/(?P<sampleId>.+)$', views.SampleView.as_view()),

    url(r'brapi/v1/phenotypes-search$', views.PhenotypeSearchView.as_view()),

    url(r'brapi/v1/studies/(?P<studyDbId>[0-9]+)/layout$', views.StudyPlotView.as_view()),

    # cannot use a ViewSet because POST is not used for creating a resource
    url(r'brapi/v1/allelematrix-search', views.AlleleMSearchView.as_view()),

    # cannot use ViewSets because one URL has the structure of a detail view, but it is not a detail view
    url(r'brapi/v1/markerprofiles/(?P<markerprofileDbId>[0-9]+)$', views.MarkerProfilesDataView.as_view()),
    url(r'brapi/v1/markerprofiles$', views.MarkerProfilesView.as_view()),

    # cannot use ViewSets because the detail view is not standard
    url(r'brapi/v1/variables/(?P<observationVariableDbId>.+)/$', views.ObsVariablesView.as_view()),
    url(r'brapi/v1/variables$', views.ObsVariablesListView.as_view()),
    url(r'brapi/v1/variables-search$', views.VSearchView.as_view()),

    url(r'brapi/v1/studies/studies-search$', views.SSearchView.as_view()),    
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observations$', views.StudyObsUnitsView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observationunits$', views.StudyObsUnitsDetailsView.as_view()),    
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/germplasm$', views.StudyGermplasmDetailsView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/table$', views.StudyObsUnitsTableView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)/observationVariables$', views.StudyObsVarsView.as_view()),
    url(r'brapi/v1/studies/(?P<studyDbId>.+)$', views.StudyDetailsView.as_view())
]

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^brapi/v1/token/(?P<backend>[^/]+)/', views.exchange_token),
    url('', include('social_django.urls', namespace='social'))
]
