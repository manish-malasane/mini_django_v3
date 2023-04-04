from django.contrib import admin

# Register your models here.

from jobs.models import Portal, JobDescription, JobTitle, Applicant

admin.site.register(Portal)
admin.site.register(JobDescription)
admin.site.register(JobTitle)
admin.site.register(Applicant)
