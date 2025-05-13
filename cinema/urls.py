from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
# from .serializers import GenreSerializer
from .views import CategoryViewSet, GenreViewSet, MovieViewSet, ShowtimeViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'Genre',  GenreViewSet)
router.register(r'Movie', MovieViewSet)
router.register(r'Show', ShowtimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
