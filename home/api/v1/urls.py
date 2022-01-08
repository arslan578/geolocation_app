from rest_framework.routers import DefaultRouter
from django.urls import path, include

from home.api.v1.viewsets import GeoLocationViewSet

router = DefaultRouter()

router.register('location', GeoLocationViewSet, basename='location')

urlpatterns = [
    path('', include(router.urls)),

]
