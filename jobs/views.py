import json
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from jobs.models import Portal, JobDescription, Applicant, JobTitle
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


# # TODO  - write an API endpoint to get list of portals (.../jobs/portal_details)
# def get_portal_details(request):
#     portals = Portal.objects.order_by("id")
#     # how to get URL associated with django-view
#
#     from django.urls import reverse
#
#     print(reverse("get_portal_details"))
#
#     por_ = []
#     for portal in portals:
#         por_.append(portal.name)
#
#     return JsonResponse(por_, safe=False)


# TODO  - write an API endpoint to get description of 1 job (.../jobs/job_detail/job_id)


def get_detail_job_desc(request, job_id):
    foo = get_object_or_404(JobDescription, pk=job_id)
    return render(request, "jobs/job_description.html", {"job_desc": foo})


# # TODO  - write an API endpoint to get list of applicants (.../jobs/applicants_details)
# def get_applicants(request):
#     applicants = []
#     foo = Applicant.objects.order_by("id")
#     for i in foo:
#         applicants.append(i.name)
#     return JsonResponse(applicants, safe=False)


# TODO  - write an API endpoint to get details of single applicant (.../jobs/applicant/1)


def get_applicant_details(request, id_):
    bar = get_object_or_404(Applicant, pk=id_)
    return render(request, "jobs/applicant_desc.html", {"appli_desc": bar})


# # TODO  - write an API endpoint to get list of titles (.../jobs/jobtitles)
# def get_titles(request):
#     titles = []
#     result = JobTitle.objects.order_by("id")
#
#     for i in result:
#         titles.append(i.title)
#     return JsonResponse(titles, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
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
        data = json.loads(request.body)
        portal_name = data.get("name")
        portal = Portal.objects.filter(name=portal_name)

        if not portal:
            portal = Portal.objects.create(**data)
            portal.save()
            return HttpResponse(f"Portal - {portal} Inserted Successfully")
        else:
            portal = Portal.objects.get(**data)
            return HttpResponse(f"Portal - {portal} is already available")

    @staticmethod
    def put(request):
        data = json.loads(request.body)
        portal_name = data.get("name")
        portal_ = Portal.objects.filter(name=portal_name)

        if not portal_:
            portal = Portal.objects.create(**data)
            portal.save()
            return HttpResponse(f"Portal- {portal} Created Successfully")
        else:
            portal = portal_.update(**data)
            return HttpResponse(f"Portal- {portal} Updated Successfully")

    @staticmethod
    def patch(request):
        data = json.loads(request.body)
        portal_name = data.get("name")
        portal_ = Portal.objects.filter(name=portal_name)

        if not portal_:
            portal = Portal.objects.create(**data)
            portal.save()
            return HttpResponse(f"Portal - {portal} Created Successfully")
        else:
            portal = portal_.update(**data)
            return HttpResponse(f"Portal- {portal} Updated Successfully")

    @staticmethod
    def delete(request):
        data = json.loads(request.body)
        portal_name = data.get("name")
        portal_ = Portal.objects.filter(name=portal_name)

        if portal_:
            portal_.delete()
            return HttpResponse("Portal Deleted Successfully")


class JobDesc(View):
    @staticmethod
    def get(request):
        roles = []
        objs = JobDescription.objects.order_by("id")

        for obj in objs:
            roles.append(obj.role)
        return render(request, "jobs/titles.html", {"roles_obj": roles})

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        jd = data.get("title")
        role = JobDescription.objects.filter(role=jd)

        if not role:
            role = JobDescription.objects.create(**data)
            role.save()
            return HttpResponse("JD Inserted Successfully")
        else:
            return HttpResponse("JD is already available")


class Titles(View):
    @staticmethod
    def get(request):
        titles = []
        objs = JobTitle.objects.order_by("id")

        for obj in objs:
            titles.append(obj.title)
        return render(request, "jobs/titles.html", {"get_titles": titles})

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        portal_data = data.get("portal")
        portal_name = portal_data.get("name")
        portal = Portal.objects.filter(name=portal_name)

        if not portal:
            portal = Portal.objects.create(**portal_data)
            portal.save()
        else:
            portal = portal[0]

        job_desc = data.get("job_description")
        jd_role = job_desc.get("role")
        jd = JobDescription.objects.filter(role=jd_role)

        if not jd:
            jd = JobDescription.objects.create(**job_desc)
            jd.save()
        else:
            jd = jd[0]

        data["portal"] = portal
        data["job_description"] = jd

        job_title = JobTitle.objects.create(**data)
        job_title.save()
        job_titles = JobTitle.objects.all()

        return render(request, "jobs/titles.html", {"titles": job_titles})

    @staticmethod
    def patch(request):
        data = json.loads(request.body)
        portal_data = data.get("portal")
        portal_name = portal_data.get("name")
        portal = Portal.objects.filter(name=portal_name)

        if not portal:
            portal = Portal.pbjects.create(**portal_data)
            portal.save()  # remove object=NOne from models.py
        else:
            portal = portal.update(**portal_data)
        job_desc = data.get("job_description")
        jd_role = job_desc.get("role")
        jd = JobDescription.objects.filter(role=jd_role)

        if not jd:
            jd = JobDescription.objects.create(**job_desc)
            jd.save()
        else:
            jd = jd.update(**job_desc)

        data["portal"] = portal
        data["job_description"] = jd

        job_title = data.get("title")
        jt = JobTitle.objects.filter(title=job_title)
        if not jt:
            jt = jt.update(**data)

        data["title"] = jt
        job_titles = JobTitle.objects.all()

        return render(request, "jobs/patch_title.html", {"patch": job_titles})
