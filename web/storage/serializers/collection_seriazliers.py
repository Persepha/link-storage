from rest_framework import serializers

from storage.serializers.link_serializers import LinkOutputSerializer
from storage.serializers.user_seriazliers import UserOutputSerializer


class CollectionOutputSerializer(serializers.Serializer):
    name = serializers.CharField()
    short_description = serializers.CharField()
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    updated_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    links = LinkOutputSerializer(many=True, read_only=True)
    user = UserOutputSerializer(read_only=True)