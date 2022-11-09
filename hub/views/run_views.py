from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime
from ..models import *
import json
import docker


class RunViewSet(viewsets.ViewSet):
    def run(self, request, pk=None):

        try:
            the_app = App.objects.get(name=pk)
        except App.DoesNotExist:
            return Response({'the status': 'name is not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            client = docker.from_env()
            the_app.envs = json.loads(the_app.envs.replace("\'", "\""))

            print('running '+the_app.name)
            client = docker.from_env()
            docker_container = client.containers.run(image=the_app.image,
                                                     command=the_app.command, environment=the_app.envs,
                                                     detach=True)
            container = Container()
            container.containerId = docker_container.id
            container.name = docker_container.name
            container.image = the_app.image
            container.command = the_app.command
            container.createdAt = datetime.now()
            container.envs = the_app.envs
            container.appName = the_app.name
            container.save()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def history(self, request):
        try:
            client = docker.from_env()
            containers_list = client.containers.list()
            print(containers_list)
            containers = Container.objects.all()
            data = []
            container_status = ""
            for container in containers:
                try:
                    docker_container = client.containers.get(container.name)
                    container_status = docker_container.status
                except:
                    container_status = "removed"
                data.append({
                    'id': container.containerId,
                    'name': container.name,
                    'image': container.image,
                    'command': container.command,
                    'envs': container.envs,
                    'createdAt': container.createdAt,
                    'status': container_status,
                    'app': container.appName,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def prune(self, request):
        try:
            client = docker.from_env()
            containers = Container.objects.all()
            for container in containers:
                try:
                    client.containers.get(container.name)
                except:
                    Container.objects.get(
                        containerId=container.containerId).delete()

            containers = Container.objects.all()
            data = []
            container_status = ""
            for container in containers:
                try:
                    docker_container = client.containers.get(container.name)
                    container_status = docker_container.status
                except:
                    container_status = "removed"
                data.append({
                    'id': container.containerId,
                    'name': container.name,
                    'image': container.image,
                    'command': container.command,
                    'envs': container.envs,
                    'createdAt': container.createdAt,
                    'status': container_status,
                    'app': container.appName,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
