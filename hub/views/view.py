
# class DockerImageCreation(APIView):
#     def post(self, request, format=None):
#         try:
#             data = request.data

#             # serializer = serializers.CreateSerializer(data=request.data)
#             # if serializer.is_valid():
#             #     name = serializer.data.get('name')
#             #     image = serializer.data.get('image')
#             #     envs = serializer.data.get('envs')
#             #     command = serializer.data.get('command')
#             # else:
#             #     return Response({'status': 'Bad Request.'}, status=status.HTTP_400_BAD_REQUEST)

#             app = App()
#             app.name = data['name']
#             app.image = data['image']
#             app.envs = data['envs']
#             app.command = data['command']
#             app.save()
#             return Response({'status': 'OK'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             print("error in exception is: ", e)
#             return Response({'status': "Internal Server Error, We'll Check It Later"},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class DockerImageRead(APIView):
#     def get(self, request, format=None):
#         try:
#             data = request.data

#             app = App()
#             app.name = data['name']
#             app.image = data['image']
#             app.envs = data['envs']
#             app.command = data['command']
#             app.save()
#             return Response({'status': 'OK'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             print("error in exception is: ", e)
#             return Response({'status': "Internal Server Error, We'll Check It Later"},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class DockerImageUpdate(APIView):
#     def put(self, request, format=None):
#         try:
#             data = request.data

#             app = App()
#             app.name = data['name']
#             app.image = data['image']
#             app.envs = data['envs']
#             app.command = data['command']
#             app.save()
#             return Response({'status': 'OK'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             print("error in exception is: ", e)
#             return Response({'status': "Internal Server Error, We'll Check It Later"},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class DockerImageDelete(APIView):
#     def delete(self, request, format=None):
#         try:
#             data = request.data
#             name = data['name']
#             App.objects.filter(name__icontains=name).delete()

#             return Response({'status': 'OK'}, status=status.HTTP_200_OK)

#         except Exception as e:
#             print("error in exception is: ", e)
#             return Response({'status': "Internal Server Error, We'll Check It Later"},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class DockerImages(APIView):
#     def get(self, request, format=None):
#         try:
#             apps = App.objects.all()
#             data = []
#             for app in apps:
#                 data.append({
#                     'name': app.name,
#                     'image': app.image,
#                     'envs': app.envs,
#                     'command': app.command,
#                 })
#             return Response({'data': data}, status=status.HTTP_200_OK)
#         except:
#             return Response({'status': "Internal Server Error, We'll Check It Later"},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)
