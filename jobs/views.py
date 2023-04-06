import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from jobs.models import Portal, JobDescription, Applicant, JobTitle
from django.views import View
from django.db.utils import IntegrityError

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


class Portals(View):
    @staticmethod
    def get(request):
        portals = []
        obj = Portal.objects.order_by("id")
        for i in obj:
            portals.append(i.name)
        return render(request, "jobs/portals.html", {"portal_obj": portals})

    @staticmethod
    def post(request):
        data = request.body
        data = json.loads(data)
        portal_name = data.get("name")
        portal = Portal.objects.filter(name=portal_name)

        if not portal:
            portal = Portal.objects.create(**data)
            portal.save()
            return HttpResponse("Portal Inserted Successfully")
        else:
            return HttpResponse("Portal is already available")

    @staticmethod
    def put(request):
        data = request.body
        data = json.loads(data)
        portal_name = data.get("name")
        portal_ = Portal.objects.filter(name=portal_name)

        if not portal_:
            portal = Portal.objects.create(**data)
            portal.save()
            return HttpResponse("Portal Created Successfully")
        else:
            portal = portal_.update(**data)
            return HttpResponse("Portal Updated Successfully")

    @staticmethod
    def patch(request):
        data = request.body
        data = json.loads(data)
        portal_name = data.get("name")
        portal_ = Portal.objects.filter(name=portal_name)

        if not portal_:
            portal = Portal.objects.create(**data)
            portal.save()
            return HttpResponse("Portal Created Successfully")
        else:
            portal = portal_.update(**data)
            return HttpResponse("Portal Updated Successfully")

    @staticmethod
    def delete(request):
        data = request.body
        data = json.loads(data)
        portal_name = data.get("name")
        portal_ = Portal.objects.filter(name=portal_name)

        if portal_:
            portal_.delete()
            return HttpResponse("Portal Deleted Successfully")


class Titles(View):
    @staticmethod
    def get(request):
        titles = []
        objs = JobTitle.objects.order_by("id")
        for obj in objs:
            titles.append(obj.title)
        return render(request, "jobs/titles.html", {"titles_obj": titles})

    @staticmethod
    def post(request):
        data = request.body
        data = json.loads(data)
        try:
            portal_data = data.get("portal")
            portal_name = portal_data.get("name")
            portal = Portal.objects.filter(name=portal_name)
            if portal:
                portal = portal[0]
            else:
                portal = Portal.objects.create(**portal_data)
                portal.save()

            jd_data = data.get("job_description")
            jd_role = jd_data.get("role")
            jd = JobDescription.objects.filter(role=jd_role)

            if jd:
                jd = jd[0]
            else:
                jd = JobDescription.objects.create(**jd_data)
                jd.save()

            data["portal"] = portal
            data["job_description"] = jd

            job_title = JobTitle.objects.create(**data)
            job_title.save()
            job_titles = JobTitle.objects.all()

            return render(request, "jobs/titles_.html", {"obj": job_titles})
        except IntegrityError as ex:
            return HttpResponse(F"eRROr {ex}")





