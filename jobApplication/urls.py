from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from jobApplication.views import JobApplicationViewSet, jobApplicationApproved, jobApplicationList, \
    jobApplicationDetail, jobApplicationListByCandidate, jobApplicationDetailByCandidate, jobApplicationCreate, \
    jobApplicationRejected

router = DefaultRouter()
router.register(r'jobApplication', JobApplicationViewSet, basename='')

urlpatterns = [
    path('jobApplication/', jobApplicationList, name='jobApplication-list'),
    path('jobApplication/<int:pk>/', jobApplicationDetail, name='jobApplication-detail'),
    path('jobApplication/candidate/', jobApplicationListByCandidate, name='jobApplication-list-by-candidate'),
    path('jobApplication/candidate/<int:pk>/', jobApplicationDetailByCandidate, name='jobApplication-detail-by'
                                                                                     '-candidate'),
    path('jobApplication/create/', jobApplicationCreate, name='jobApplication-create'),
    path('jobApplication/approved/<int:pk>/', jobApplicationApproved, name='jobApplication-approved'),
    path('jobApplication/rejected/<int:pk>/', jobApplicationRejected, name='jobApplication-rejected'),
]
