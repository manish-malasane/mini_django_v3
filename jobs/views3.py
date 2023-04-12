import json

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Portal


class Portals(APIView):
    def get(self, request):
        portals = Portal.objects.all()
        final = dict()
        for portal in portals:
            final[portal.id] = {"name": portal.name, "description": portal.description}
        return Response(final)

    def post(self, request):
        data = json.loads(request.body)
        portal = Portal.objects.create(**data)
        return Response("portal created")


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        final = dict()
        for user in users:
            final[user.id] = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        return Response(final)
