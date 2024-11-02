from typing import Iterable

from common.exceptions import ApplicationError
from django.conf import settings
from django.shortcuts import get_object_or_404
from storage.models.collection import Collection
from storage.models.link import Link


def get_links_by_ids(*, links_ids: str) -> Iterable[Link]:
    ids = links_ids.strip(",").split(",")

    links = []

    for id_ in ids:
        try:
            link_id = int(id_.strip())
        except Exception as e:
            raise ApplicationError(
                "Incorrect link id",
                extra={"fields": f"{id_} - Incorrect value for link id"},
            )
        obj = get_object_or_404(Link, id=link_id)
        links.append(obj)

    return links


def collection_create(
    *,
    name: str,
    short_description: str,
    user: settings.AUTH_USER_MODEL,
    links_ids: str = None,
) -> Collection:
    collection = Collection(name=name, short_description=short_description, user=user)
    collection.full_clean()
    collection.save()

    if links_ids is not None:
        link_list: Iterable[Link] = get_links_by_ids(links_ids=links_ids)
        collection.links.add(*link_list)

    return collection


def collection_delete(*, collection: Collection):
    collection.delete()
