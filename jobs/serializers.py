from rest_framework import serializers
from jobs.models import Portal, JobTitle, JobDescription, Applicant
from django.utils import timezone



class PortalSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Portal.objects.create(**validated_data)


class JobDescriptionSerializer(serializers.Serializer):
    role = serializers.CharField(max_length=50)
    description_text = serializers.CharField(max_length=150)
    published_date = serializers.DateTimeField(default=timezone.now())

    def create(self, validated_data):
        return JobDescription.objects.create(**validated_data)


class JobTitleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    last_updated = serializers.DateTimeField(default=timezone.now())
    job_description = JobDescriptionSerializer(required=False)
    portal = PortalSerializer(required=False)

    def create(self, validated_data):
        return JobTitle.objects.create(**validated_data)


class ApplicantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    applied_for = JobTitleSerializer(required=False)
    cover_letter = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Applicant.objects.create(**validated_data)
