from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ComediansViewSet, JokesViewSet

router = DefaultRouter()
router.register("comedians", ComediansViewSet)
router.register("jokes", JokesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
