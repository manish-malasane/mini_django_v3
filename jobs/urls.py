"""minidjango_v4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the, include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from . import views2

urlpatterns = [
    path("job_detail/<int:job_id>", views.get_detail_job_desc, name="get_job_detail"),
    path(
        "applicant/<int:id_>", views.get_applicant_details, name="get_applicant_details"
    ),
    path("portals/", views.Portals.as_view(), name="portals"),
    path("titles/", views.Titles.as_view(), name="titles"),
    path("v2/applicants/", views2.ApplicantList.as_view(), name="applicant-list"),
    path("v2/applicants/create/", views2.ApplicantCreate.as_view(), name="applicant-create"),
    path("v2/applicants/detail/<int:pk>", views2.ApplicantDetail.as_view(), name="applicant-detail"),
    path("v2/applicants/update/<int:pk>", views2.ApplicantUpdate.as_view(), name="applicant-update"),
    path("v2/applicants/delete/<int:pk>", views2.ApplicantDelete.as_view(), name="applicant-delete"),
    path("v2/portals/", views2.PortalList.as_view(), name="portal-list"),
    path("v2/portals/create/", views2.PortalCreate.as_view(), name="portal-create"),
    path("v2/portals/detail/<int:pk>", views2.PortalDetail.as_view(), name="portal-detail"),
    path("v2/portals/update/<int:pk>", views2.PortalUpdate.as_view(), name="portal-update"),
    path("v2/portals/delete/<int:pk>", views2.PortalDelete.as_view(), name="portal-delete"),
    path("v2/jobtitles/", views2.JobTitleList.as_view(), name="job-title-list"),
    path("v2/jobtitles/create/", views2.JobTitleCreate.as_view(), name="job-title-create"),
    path("v2/jobtitles/detail/<int:pk>", views2.JobTitleDetail.as_view(), name="job-title-detail"),
    path("v2/jobtitles/update/<int:pk>", views2.JobTitleUpdate.as_view(), name="job-title-update"),
    path("v2/jobtitles/delete/<int:pk>", views2.JobTitleDelete.as_view(), name="job-title-delete"),
    path("v2/jd/", views2.JobDescriptionList.as_view(), name="job-description-list"),
    path("v2/jd/create/", views2.JobDescriptionCreate.as_view(), name="job-description-create"),
    path("v2/jd/detail/<int:pk>", views2.JobDescriptionDetail.as_view(), name="job-description-detail"),
    path("v2/jd/update/<int:pk>", views2.JobDescriptionUpdate.as_view(), name="job-description-update"),
    path("v2/jd/delete/<int:pk>", views2.JobDescriptionDelete.as_view(), name="job-description-delete"),
]
