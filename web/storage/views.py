from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from storage.selectors import link_list
from storage.serializers import FilterSerializer, LinkOutputSerializer


class LinkListApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        tasks = link_list(filters=filters_serializer.validated_data)

        data = LinkOutputSerializer(tasks, many=True).data

        return Response(data)
