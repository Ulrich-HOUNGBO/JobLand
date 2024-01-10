from rest_framework import serializers
from .models import Job, Category, JobType


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['id', 'name']


class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    job_type = JobTypeSerializer()

    class Meta:
        model = Job
        fields = '__all__'
