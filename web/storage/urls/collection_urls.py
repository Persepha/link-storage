from django.urls import path

from storage.views.collection_views import CollectionListApi

urlpatterns = [
    path("", CollectionListApi.as_view(), name="collection-list"),
]