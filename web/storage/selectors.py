from django.db.models import QuerySet

from storage.filters import BaseCollectionFilter, BaseLinkFilter
from storage.models.collection import Collection
from storage.models.link import Link


def link_list(*, filters=None) -> QuerySet[Link]:
    filters = filters or {}

    qs = Link.objects.all()

    return BaseLinkFilter(filters, qs).qs


def collection_list(*, filters=None) -> QuerySet[Collection]:
    filters = filters or {}

    qs = Collection.objects.all()

    return BaseCollectionFilter(filters, qs).qs