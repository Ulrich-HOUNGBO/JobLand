# Generated by Django 5.0 on 2023-12-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApplication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resume/'),
        ),
    ]