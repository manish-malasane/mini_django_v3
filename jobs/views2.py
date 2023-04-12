from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from jobs.models import Applicant, Portal, JobTitle, JobDescription
from django.urls import reverse_lazy


# Generic views for applicant table
class ApplicantList(ListView):
    model = Applicant


class ApplicantCreate(CreateView):
    model = Applicant
    fields = ["name", "applied_for", "cover_letter"]
    success_url = reverse_lazy("applicant-list")


class ApplicantDetail(DetailView):
    model = Applicant
    context_object_name = "applicant"
    queryset = Applicant.objects.all()


class ApplicantUpdate(UpdateView):
    model = Applicant
    fields = ["id", "name", "cover_letter"]
    success_url = reverse_lazy("applicant-list")


class ApplicantDelete(DeleteView):
    model = Applicant
    success_url = reverse_lazy("applicant-list")


# Generic views for portal table


class PortalList(ListView):
    model = Portal


class PortalDetail(DetailView):
    model = Portal
    context_object_name = "portal"
    queryset = Portal.objects.all()


class PortalCreate(CreateView):
    model = Portal
    fields = ["name", "description"]
    success_url = reverse_lazy("portal-list")


class PortalUpdate(UpdateView):
    model = Portal
    fields = ["description"]
    success_url = reverse_lazy("portal-list")


class PortalDelete(DeleteView):
    model = Portal
    success_url = reverse_lazy("portal-list")


# Generic views for job title table


class JobTitleList(ListView):
    model = JobTitle


class JobTitleDetail(DetailView):
    model = JobTitle
    context_object_name = "title"
    queryset = JobTitle.objects.all()


class JobTitleCreate(CreateView):
    model = JobTitle
    fields = ["title", "job_description", "portal"]
    success_url = reverse_lazy("job-title-list")


class JobTitleUpdate(UpdateView):
    model = JobTitle
    fields = ["job_description", "portal"]
    success_url = reverse_lazy("job-title-list")


class JobTitleDelete(DeleteView):
    model = JobTitle
    success_url = reverse_lazy("job-title-list")


# Generic views for job description table


class JobDescriptionList(ListView):
    model = JobDescription


class JobDescriptionDetail(DetailView):
    model = JobDescription
    context_object_name = "role"
    queryset = JobDescription.objects.all()


class JobDescriptionCreate(CreateView):
    model = JobDescription
    fields = ["role", "description_text"]
    success_url = reverse_lazy("job-description-list")


class JobDescriptionUpdate(UpdateView):
    model = JobDescription
    fields = ["role", "description_text"]
    success_url = reverse_lazy("job-description-list")


class JobDescriptionDelete(DeleteView):
    model = JobDescription
    success_url = reverse_lazy("job-description-list")
