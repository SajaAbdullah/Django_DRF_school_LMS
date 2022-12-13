from django.urls import path
from rest_framework.routers import DefaultRouter

from .mongo_views import MongoTeacherViewSet

# Create a router and register our viewsets with it the router will work for all crud calls.
router = DefaultRouter()
router.register("crud_api", MongoTeacherViewSet, basename="crud_api")

urlpatterns = router.urls
