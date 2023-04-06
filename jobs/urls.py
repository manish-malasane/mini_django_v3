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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path("portal_details/", views.get_portal_details, name="get_portal_details"),
    path("job_detail/<int:job_id>", views.get_detail_job_desc, name="get_job_detail"),
    path("applicants_details", views.get_applicants, name="get_applicants"),
    path(
        "applicant/<int:id_>", views.get_applicant_details, name="get_applicant_details"
    ),
    path("job_titles/", views.get_titles, name="job_titles"),
    path("portals/", views.Portals.as_view(), name="portals"),
]
