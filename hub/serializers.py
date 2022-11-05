from unicodedata import category
from rest_framework import serializers

from hub.models import App


class CreateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    image = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)
    envs = serializers.FileField(required=True, allow_null=False, allow_empty_file=False)
    command = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=128)