from jobs.models import Portal, Applicant, JobTitle, JobDescription
from jobs.serializers import PortalSerializer, ApplicantSerializer, JobTitleSerializer, JobDescriptionSerializer
from django.http import JsonResponse


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
        return JsonResponse(obj.data, safe=False)


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
