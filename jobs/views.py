from django.shortcuts import render
from django.http import JsonResponse
from jobs.models import Portal

# Create your views here.


def get_portal_details(request):
    portals = Portal.objects.order_by()
    # how to get URL associated with django-view

    from django.urls import reverse

    print(reverse("get_portal_details"))

    por_ = []
    for portal in portals:
        por_.append(portal.name)

    return JsonResponse(por_, safe=False)





