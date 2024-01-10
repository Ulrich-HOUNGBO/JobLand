
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from JobList.views import JobViewSet

router = DefaultRouter()
router.register(r'joblist', JobViewSet, basename='')

urlpatterns = [
    path('', include(router.urls)),
]
