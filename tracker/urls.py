from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, EmissionFactorViewSet, ActivityLogViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet, basename='userprofile')
router.register(r'emissionfactors', EmissionFactorViewSet, basename='emissionfactor')
router.register(r'activitylogs', ActivityLogViewSet, basename='activitylog')

urlpatterns = [
    path('', include(router.urls)),
]
