from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from ..models import *

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from datetime import datetime


class RunViewSet(viewsets.ViewSet):
    def run(self, request, pk=None):
        try:
            name = pk
            the_app = ""

            try:
                the_app = App.objects.get(name=name)
            except App.DoesNotExist:
                return Response({'the status': 'name is not found.'}, status=status.HTTP_400_BAD_REQUEST)

            history = History()
            history.name = the_app.name
            history.envs = the_app.envs
            history.startAt = datetime.now()
            history.save()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def history(self, request):
        try:
            histories = History.objects.all()
            data = []
            for history in histories:
                isRunning = False
                data.append({
                    'name': history.name,
                    'envs': history.envs,
                    'startAt': history.startAt,
                    'isRunning': isRunning,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
