from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from jobApplication.models import JobApplication
from jobApplication.serializers import JobApplicationSerializer

from rest_framework.decorators import api_view, permission_classes, parser_classes

from jobLand.permissions import IsEmployer, IsCandidate

file_param = openapi.Parameter('resume', openapi.IN_FORM, description='Fichier du CV', type=openapi.TYPE_FILE)
job_param = openapi.Parameter('job', openapi.IN_FORM, description='ID du job', type=openapi.TYPE_STRING)
status_param = openapi.Parameter('status', openapi.IN_FORM, description='Statut de la candidature',
                                 type=openapi.TYPE_STRING)


# Create your views here.

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def jobApplicationList(request):
    jobApplications = JobApplication.objects.all()
    serializer = JobApplicationSerializer(jobApplications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def jobApplicationDetail(request, pk):
    jobApplication = JobApplication.objects.get(id=pk)
    serializer = JobApplicationSerializer(jobApplication, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsCandidate])
def jobApplicationListByCandidate(request):
    jobApplications = JobApplication.objects.filter(user=request.user)
    serializer = JobApplicationSerializer(jobApplications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsCandidate])
def jobApplicationDetailByCandidate(request, pk):
    jobApplication = JobApplication.objects.get(id=pk)
    serializer = JobApplicationSerializer(jobApplication, many=False)
    return Response(serializer.data)


@swagger_auto_schema(method='post', manual_parameters=[file_param, job_param, status_param])
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsEmployer])
@parser_classes([MultiPartParser])
def jobApplicationCreate(request):
    data = request.data
    jobApplication = JobApplication.objects.create(
        job=data['job'],
        user=request.user,
        resume=data['resume'],
        status=data['status'],
    )
    serializer = JobApplicationSerializer(jobApplication, many=False)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsEmployer])
def jobApplicationApproved(request, pk):
    jobApplication = JobApplication.objects.get(id=pk)
    jobApplication.status = 'approved'  # Update the status to 'approved'
    jobApplication.save()  # Save the changes
    serializer = JobApplicationSerializer(jobApplication, many=False)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated, IsEmployer])
def jobApplicationRejected(request, pk):
    jobApplication = JobApplication.objects.get(id=pk)
    jobApplication.status = 'rejected'  # Update the status to 'rejected'
    jobApplication.save()  # Save the changes
    serializer = JobApplicationSerializer(jobApplication, many=False)
    return Response(serializer.data)
