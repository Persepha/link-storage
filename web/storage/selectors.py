from django.db.models import QuerySet

from storage.filters import BaseTaskFilter
from storage.models.link import Link


def link_list(*, filters=None) -> QuerySet[Link]:
    filters = filters or {}

    qs = Link.objects.all()

    return BaseTaskFilter(filters, qs).qs
