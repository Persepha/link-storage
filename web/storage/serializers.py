from rest_framework import serializers


class LinkOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    link_type = serializers.CharField(source="get_link_type_display", read_only=True)
    short_description = serializers.CharField()
    url = serializers.URLField()
    image = serializers.URLField()
    created_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    updated_at = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    user_username = serializers.CharField(source="user.username", read_only=True)


class LinkInputSerializer(serializers.Serializer):
    url = serializers.URLField()


class FilterSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False, max_length=255)
