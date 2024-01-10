import uuid

from django.db import models


# Create your models here.

class JobApplication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey('JobList.Job', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="pending")
    resume = models.FileField(upload_to="resume/", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.job

    def __repr__(self):
        return self.job

    class Meta:
        db_table = "job_application"
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"
