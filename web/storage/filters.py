import django_filters

from storage.models.collection import Collection
from storage.models.link import Link


class BaseLinkFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ("id", "title")


class BaseCollectionFilter(django_filters.FilterSet):
    class Meta:
        model = Collection
        fields = ("id", "name")
