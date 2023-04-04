from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from jobs.models import Portal, JobDescription, Applicant, JobTitle

# Create your views here.


# TODO  - write an API endpoint to get list of portals (.../jobs/portal_details)


def get_portal_details(request):
    portals = Portal.objects.order_by("id")
    # how to get URL associated with django-view

    from django.urls import reverse

    print(reverse("get_portal_details"))

    por_ = []
    for portal in portals:
        por_.append(portal.name)

    return JsonResponse(por_, safe=False)


# TODO  - write an API endpoint to get description of 1 job (.../jobs/job_detail/job_id)


def get_detail_job_desc(request, job_id):
    foo = get_object_or_404(JobDescription, pk=job_id)
    return render(request, "jobs/job_description.html", {"job_desc": foo})


# TODO  - write an API endpoint to get list of applicants (.../jobs/applicants_details)


def get_applicants(request):
    applicants = []
    foo = Applicant.objects.order_by("id")
    for i in foo:
        applicants.append(i.name)
    return JsonResponse(applicants, safe=False)


# TODO  - write an API endpoint to get details of single applicant (.../jobs/applicant/1)


def get_applicant_details(request, id_):
    bar = get_object_or_404(Applicant, pk=id_)
    return render(request, "jobs/applicant_desc.html", {"appli_desc": bar})


# TODO  - write an API endpoint to get list of titles (.../jobs/jobtitles)


def get_titles(request):
    titles = []
    result = JobTitle.objects.order_by("id")

    for i in result:
        titles.append(i.title)
    return JsonResponse(titles, safe=False)
