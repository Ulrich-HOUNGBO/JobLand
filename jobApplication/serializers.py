from rest_framework import serializers

from jobApplication.models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobApplication
        fields = '__all__'
