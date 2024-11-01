from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from storage.models.link import Link
from storage.permissions import IsOwner
from storage.selectors import link_list
from storage.serializers import (
    FilterSerializer,
    LinkInputSerializer,
    LinkOutputSerializer, LinkUpdateInputSerializer,
)
from storage.services import link_create, link_delete, link_update


class LinkListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        tasks = link_list(filters=filters_serializer.validated_data)

        data = LinkOutputSerializer(tasks, many=True).data

        return Response(data)


@extend_schema(request=LinkInputSerializer)
class LinkCreateApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = LinkInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user

        created_task = link_create(**serializer.validated_data, user=user)

        return Response(status=status.HTTP_201_CREATED)


class LinkDeleteApi(APIView):
    permission_classes = (IsOwner | IsAdminUser,)

    def delete(self, request, id):
        link = get_object_or_404(Link, id=id)

        self.check_object_permissions(request, link)

        link_delete(link=link)

        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(request=LinkUpdateInputSerializer)
class LinkUpdateApi(APIView):
    permission_classes = (IsOwner | IsAdminUser,)

    def post(self, request, id):
        serializer = LinkUpdateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        link = get_object_or_404(Link, id=id)

        self.check_object_permissions(request, link)

        updated_task, _ = link_update(link=link, data=serializer.validated_data)

        return Response(status=status.HTTP_200_OK)