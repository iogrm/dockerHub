from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from ..models import App
from .. import serializers

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

import json


class HubViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            data = request.data

            app = App()
            app.name = data['name']
            app.image = data['image']
            app.envs = data['envs']
            app.command = data['command']
            app_with_name = App.objects.filter(name=app.name)
            if app_with_name:
                return Response({'the status': 'name is used before.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                app.save()
                return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, pk=None):
        try:
            name = pk
            the_app = ""
            try:
                the_app = App.objects.get(name=name)
            except App.DoesNotExist:
                return Response({'the status': 'name is not found.'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({'data': {'name': the_app.name, 'envs': the_app.envs}}, status=status.HTTP_200_OK)
        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def edit(self, request):
        try:
            data = request.data
            name = data['name']
            the_app = ""
            try:
                the_app = App.objects.get(name=name)
            except App.DoesNotExist:
                return Response({'the status': 'name is not found.'}, status=status.HTTP_400_BAD_REQUEST)
            the_app.image = data['image']
            the_app.envs = data['envs']
            the_app.command = data['command']
            the_app.save()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def remove(self, request):
        try:
            data = request.data
            name = data['name']
            print(name)
            app = App.objects.filter(name=name).delete()
            print(app)
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def getAll(self, request):
        try:
            apps = App.objects.all()
            data = []
            for app in apps:
                data.append({
                    'name': app.name,
                    'image': app.image,
                    'envs': app.envs,
                    'command': app.command,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
