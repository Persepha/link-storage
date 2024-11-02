from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from storage.models.collection import Collection
from storage.selectors import collection_list
from storage.serializers.collection_seriazliers import CollectionOutputSerializer, CollectionInputSerializer
from storage.serializers.link_serializers import FilterSerializer
from storage.services.collection_services import collection_create


class CollectionListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        collections = collection_list(filters=filters_serializer.validated_data)

        data = CollectionOutputSerializer(collections, many=True).data

        return Response(data)


@extend_schema(request=CollectionInputSerializer)
class CollectionCreateApi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CollectionInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.request.user

        links_ids = None
        if 'links_ids' in request.data:
            links_ids = serializer.validated_data.pop('links_ids')

        created_collection = collection_create(**serializer.validated_data,
                                     user=user, links_ids=links_ids)

        return Response(status=status.HTTP_201_CREATED)


class CollectionDetailApi(APIView):
    def get(self, request, id):
        collection = get_object_or_404(Collection, id=id)
        serializer = CollectionOutputSerializer(collection)

        return Response(serializer.data)