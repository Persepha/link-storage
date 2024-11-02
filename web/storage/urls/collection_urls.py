from django.urls import path
from storage.views.collection_views import (
    CollectionCreateApi,
    CollectionDeleteApi,
    CollectionDetailApi,
    CollectionListApi,
    CollectionUpdateApi,
)

urlpatterns = [
    path("", CollectionListApi.as_view(), name="collection-list"),
    path("create/", CollectionCreateApi.as_view(), name="collection-create"),
    path("<int:id>/", CollectionDetailApi.as_view(), name="collection-detail"),
    path("<int:id>/delete/", CollectionDeleteApi.as_view(), name="collection-delete"),
    path("<int:id>/update/", CollectionUpdateApi.as_view(), name="collection-update"),
]
