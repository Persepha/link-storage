from django.urls import path

from storage.views import LinkCreateApi, LinkDeleteApi, LinkListApi

urlpatterns = [
    path("", LinkListApi.as_view(), name="link-list"),
    path("create/", LinkCreateApi.as_view(), name="link-create"),
    path("<int:id>/delete/", LinkDeleteApi.as_view(), name="link-delete"),
]
