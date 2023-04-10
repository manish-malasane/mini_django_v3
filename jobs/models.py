from django.db import models
from django.utils import timezone

# Create your models here.


class Portal(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class JobDescription(models.Model):
    role = models.CharField(max_length=250)
    description_text = models.CharField(max_length=500)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.role} - ({self.published_date})"


class JobTitle(models.Model):
    title = models.CharField(max_length=250)
    last_updated = models.DateTimeField(default=timezone.now)

    # one-to-one relationship (here job title description is unique against each  job title)
    job_description = models.OneToOneField(JobDescription, on_delete=models.CASCADE)

    # one-to-many relationship (here job title is unique but, it is available on multiple portals)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - ({self.portal})"


class Applicant(models.Model):
    name = models.CharField(max_length=250)

    # ONE-TO-MANY relationship (here applicant is applied for multiple job titles)
    applied_for = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    cover_letter = models.CharField(max_length=500)

    def __str__(self):
        return self.name
