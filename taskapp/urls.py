from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()                             #Automatically generating URL patterns for viewsets.
router.register(r'', TaskViewSet, basename='task')   #Registers TaskViewSet with the router.

urlpatterns = router.urls
