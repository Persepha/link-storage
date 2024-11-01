from django.urls import path

from storage.views import LinkListApi

urlpatterns = [
    path("", LinkListApi.as_view(), name="link-list")
]