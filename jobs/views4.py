from jobs.models import Portal, Applicant, JobTitle, JobDescription
from jobs.serializers import (
    PortalSerializer,
    ApplicantSerializer,
    JobTitleSerializer,
    JobDescriptionSerializer,
)
from django.http import JsonResponse
import json
from rest_framework.parsers import JSONParser


def portal_list(request):
    if request.method == "GET":
        portals = Portal.objects.all()

        # How to serialize multiple objects using DRF serializer
        obj = PortalSerializer(portals, many=True)

        # from serialized object pull out only the data by using `data` attribute on serialized object
        # Whenever our data is in non-dict format we have pass addition arg called safe=False
        return JsonResponse(obj.data, safe=False)


def applicant_list(request):
    if request.method == "GET":
        applicants = Applicant.objects.all()

        obj = ApplicantSerializer(applicants, many=True)

        # how to validate serialized objects against validation constraints?
        data = ApplicantSerializer(data=obj.data, many=True)
        print(data.is_valid())

        # How to check errors
        # print(obj.errors)
        return JsonResponse(obj.data, safe=False)

    if request.method == "POST":
        # 1st way
        using_json_module = json.loads(request.body)

        # 2nd way
        parser = JSONParser
        data = parser.parse(request)


def job_title_list(request):
    if request.method == "GET":
        job_titles = JobTitle.objects.all()

        obj = JobTitleSerializer(job_titles, many=True)
        return JsonResponse(obj.data, safe=False)


def job_description_list(request):
    if request.method == "GET":
        job_descriptions = JobDescription.objects.all()

        obj = JobDescriptionSerializer(job_descriptions, many=True)
        return JsonResponse(obj.data, safe=False)
