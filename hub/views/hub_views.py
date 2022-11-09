
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from hub.serializers import *
from ..models import App


class HubViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            data = request.data
            serializer = AppSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
                the_app = App.objects.filter(
                    name=serializer.validated_data['name'])
                if the_app:
                    return Response({'status': 'name is used before.'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    serializer.save()
                    return Response({'status': 'OK'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def getApp(self, request, pk=None):

        try:
            the_app = App.objects.get(name=pk)
        except App.DoesNotExist:
            return Response({'status': 'name is not found.'}, status=status.HTTP_404_NOT_FOUND)
        try:
            serializer = AppSerializer(the_app)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def edit(self, request, pk=None):
        try:
            the_app = App.objects.get(name=pk)
        except App.DoesNotExist:
            return Response({'status': 'name is not found.'}, status=status.HTTP_404_NOT_FOUND)
        try:
            data = request.data
            serializer = EditAppSerializer(the_app, data=data)
            if serializer.is_valid():
                try:
                    if data['name'] != pk:
                        return Response({'status': 'app name is not same'}, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    print("error in exception is: ", e)
                serializer.save()
                return Response({'status': 'OK'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk=None):
        try:
            App.objects.get(name=pk).delete()
            return Response({'status': 'OK'}, status=status.HTTP_200_OK)

        except App.DoesNotExist:
            return Response({'status': 'name is not found.'}, status=status.HTTP_404_NOT_FOUND)

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
        except Exception as e:
            print("error in exception is: ", e)
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
