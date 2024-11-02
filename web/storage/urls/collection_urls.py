from django.urls import path

from storage.views.collection_views import CollectionListApi, CollectionCreateApi, CollectionDetailApi

urlpatterns = [
    path("", CollectionListApi.as_view(), name="collection-list"),
    path("create/", CollectionCreateApi.as_view(), name="collection-create"),
    path("<int:id>/", CollectionDetailApi.as_view(), name="collection-detail"),
]
