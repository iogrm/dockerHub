from rest_framework import serializers

from hub.models import App


class AppSerializer(serializers.ModelSerializer):
    envs = serializers.JSONField()

    class Meta:
        model = App
        fields = ['name', 'image', 'envs', 'command']


class EditAppSerializer(serializers.ModelSerializer):
    envs = serializers.JSONField()

    class Meta:
        model = App
        fields = ['image', 'envs', 'command']
