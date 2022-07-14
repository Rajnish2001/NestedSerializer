from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('singerapi/',views.SingerViewSet,basename='Singer')
router.register('songapi/',views.SongViewSet,basename='Song')

urlpatterns = [
    path('',include(router.urls)),
]
