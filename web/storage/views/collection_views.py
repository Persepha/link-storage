from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from storage.selectors import collection_list
from storage.serializers.collection_seriazliers import CollectionOutputSerializer
from storage.serializers.link_serializers import FilterSerializer


class CollectionListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        collections = collection_list(filters=filters_serializer.validated_data)

        data = CollectionOutputSerializer(collections, many=True).data

        return Response(data)