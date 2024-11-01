import django_filters

from storage.models.link import Link


class BaseTaskFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ("id", "title")
