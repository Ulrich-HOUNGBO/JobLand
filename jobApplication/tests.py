import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from jobApplication.models import JobApplication
from mixer.backend.django import mixer


@pytest.mark.django_db
def test_jobApplicationList_returns_all_job_applications():
    # Setup
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')

    mixer.blend(JobApplication, user=user)
    mixer.blend(JobApplication, user=user)

    # Execute
    response = client.get('/jobApplicationList/')

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.django_db
def test_jobApplicationList_returns_empty_when_no_job_applications():
    # Setup
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='12345')
    client.login(username='testuser', password='12345')

    # Execute
    response = client.get('/jobApplicationList/')

    # Assert
    assert response.status_code == 200
    assert len(response.json()) == 0


@pytest.mark.django_db
def test_jobApplicationList_returns_unauthorized_when_not_authenticated():
    # Setup
    client = APIClient()

    # Execute
    response = client.get('/jobApplicationList/')

    # Assert
    assert response.status_code == 401
