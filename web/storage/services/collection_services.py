from typing import Iterable, Tuple

from common.exceptions import ApplicationError
from common.services import model_update
from django.conf import settings
from django.db import transaction
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


@transaction.atomic
def collection_update(
    *,
    collection: Collection,
    data,
) -> Tuple[Collection, bool]:
    non_side_effect_fields = [
        "name",
        "short_description",
    ]

    collection, has_updated = model_update(
        instance=collection,
        fields=non_side_effect_fields,
        data=data,
    )

    if "links_ids" in data:
        link_list: Iterable[Link] = get_links_by_ids(links_ids=data["links_ids"])
        collection.links.set(link_list)

    return collection, has_updated
