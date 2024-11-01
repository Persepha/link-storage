from django.conf import settings
from django.db import transaction

from storage.models.link import Link


def link_create(*, url: str, user: settings.AUTH_USER_MODEL) -> Link:
    link = Link(url=url, user=user)
    link.full_clean()
    link.save()

    return link


def link_delete(*, link: Link):
    link.delete()


@transaction.atomic
def link_update(*, link: Link, data) -> Link:
    pass
