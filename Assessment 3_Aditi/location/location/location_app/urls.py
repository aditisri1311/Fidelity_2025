from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  LocationViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='location')

# Include the router URLs
urlpatterns = [
    path('app/', include(router.urls)),  
]
