from jobs.models import Portal, Applicant, JobTitle, JobDescription
from jobs.serializers import (
    PortalSerializer,
    ApplicantSerializer,
    JobTitleSerializer,
    JobDescriptionSerializer,
)
from django.http import JsonResponse, HttpResponse
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

    if request.method == "POST":
        data = json.loads(request.body)

        serialized_portal = PortalSerializer(data=data)
        if serialized_portal.is_valid():
            Portal.objects.create(**data)

        return JsonResponse(serialized_portal.data)

    if request.method == "DELETE":
        data = json.loads(request.body)

        serialized_portal = PortalSerializer(data=data)
        if serialized_portal.is_valid():
            obj = Portal.objects.filter(**data)
            obj.delete()

        return JsonResponse(serialized_portal.data)


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

    if request.method == "POST":  # Not completed yet
        # 1st way
        data = json.loads(request.body)

        # # 2nd way
        # parser = JSONParser()
        # data = parser.parse(request)
        applied_for = data.get("applied_for")  # jobtitle relation
        obj = JobTitleSerializer(data=applied_for)

        foo = None
        if obj.is_valid():
            foo = obj.save()

        serialized_applicant = ApplicantSerializer(data=data)
        if serialized_applicant.is_valid():
            data["applied_for"] = foo
            Applicant.objects.create(**data)

        return JsonResponse(serialized_applicant.data)


def job_title_list(request):
    if request.method == "GET":
        job_titles = JobTitle.objects.all()

        obj = JobTitleSerializer(job_titles, many=True)
        return JsonResponse(obj.data, safe=False)

    if request.method == "POST":
        # 1st way
        data = json.loads(request.body)

        # # 2nd way
        # parser = JSONParser()
        # data = parser.parse(request)
        jd_data = data.get("job_description")
        serialized_jd = JobDescriptionSerializer(data=jd_data)

        jd_obj = None
        if serialized_jd.is_valid():
            jd_obj = serialized_jd.save()

        portal_obj = None
        portal_data = data.get("portal")
        serialized_portal = PortalSerializer(data=portal_data)

        if serialized_portal.is_valid():
            portal_obj = serialized_portal.save()

        serialized_jt = JobTitleSerializer(data=data)
        if serialized_jt.is_valid():
            data["job_description"] = jd_obj
            data["portal"] = portal_obj
            JobTitle.objects.create(**data)

        return JsonResponse(serialized_jt.data, safe=False)

    if request.method == "DELETE":
        parser = JSONParser()
        data = parser.parse(request)

        serialized_jt = JobTitleSerializer(data=data)
        if serialized_jt.is_valid():
            obj = JobTitle.objects.get(**data)
            obj.delete()

            # pass id in postman like job_description_id, portal_id

        return JsonResponse(serialized_jt.data)


def job_description_list(request):
    if request.method == "GET":
        job_descriptions = JobDescription.objects.all()

        obj = JobDescriptionSerializer(job_descriptions, many=True)
        return JsonResponse(obj.data, safe=False)

    if request.method == "POST":
        data = json.loads(request.body)

        serialized_jd = JobDescriptionSerializer(data=data)

        if serialized_jd.is_valid():
            JobDescription.objects.create(**data)

        return JsonResponse(serialized_jd.data)

    if request.method == "DELETE":
        data = json.loads(request.body)

        serialized_jd = JobDescriptionSerializer(data=data)

        if serialized_jd.is_valid():
            obj = JobDescription.objects.filter(**data)
            obj.delete()

        return JsonResponse(serialized_jd.data)
