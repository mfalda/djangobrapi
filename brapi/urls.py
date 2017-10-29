from django.conf.urls import url, include
from brapi import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from brapi.views import (CallsViewSet, LocationViewSet, CropViewSet, 
    MapViewSet, MapLinkageView, MapLinkageViewPositions, MarkerViewSet, TraitViewSet)


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
router.register(r'brapi/v1/calls', views.CallsViewSet, 'calls')
router.register(r'brapi/v1/locations', views.LocationViewSet, 'locations')
router.register(r'brapi/v1/programs', views.ProgramViewSet, 'programs')
router.register(r'brapi/v1/maps', views.MapViewSet, 'maps')
router.register(r'brapi/v1/markers', views.MarkerViewSet, 'markers')
router.register(r'brapi/v1/traits', views.TraitViewSet, 'traits')

# The API URLs are now determined automatically by the router
# Additionally, we include the login URLs for the browsable API
urlpatterns = [
    url(r'^', include(router.urls)),
    # cannot use ViewSets because the detail view is not standard
    url(r'brapi/v1/maps/(?P<mapDbId>.+)/positions/$', views.MapLinkageView.as_view()),
    url(r'brapi/v1/maps/(?P<mapDbId>.+)/positions/(?P<linkageGroupId>[0-9]+)/$', views.MapLinkageViewPositions.as_view()),
]

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^schema/$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls')),
]
