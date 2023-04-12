import json

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Portal
from .serializers import PortalSerializer
from rest_framework.parsers import JSONParser


class Portals(APIView):
    def get(self, request):
        portals = Portal.objects.all()
        final = dict()
        for portal in portals:
            final[portal.id] = {"name": portal.name, "description": portal.description}
        return Response(final)

    def post(self, request):
        data = json.loads(request.body)

        serialized_portal = PortalSerializer(data=data)

        if serialized_portal.is_valid():
            obj = Portal.objects.create(**data)
            resp = {
                "name": obj.name,
                "description": obj.description,
                "message": f"{obj} inserted successfully"
            }

            return Response(resp)

    def delete(self, request):
        parser = JSONParser()
        data = parser.parse(request)

        serialized_portal = PortalSerializer(data=data)

        if serialized_portal.is_valid():
            obj = Portal.objects.filter(**data)
            obj.delete()

            resp = {
                "message": f"{obj.name} - portal deleted successfully"
            }
            return Response(resp)


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
