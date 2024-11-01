from django.conf import settings
from django.db import transaction
from metadata_parser import MetadataParser

from common.exceptions import ApplicationError
from storage.models.link import Link


def get_url_data(url: str):
    data = {
        "title": None,
        "short_description": None,
        "image": None,
        "link_type": "website",
    }

    try:
        page = MetadataParser(url=url)
    except Exception as e:
        raise ApplicationError(
            message="Error while getting data from url", extra={"msg": e.message}
        )
    else:
        title = page.get_metadata("title", strategy=["og", "dc", "meta", "page"])
        description = page.get_metadata(
            "description", strategy=["og", "dc", "meta", "page"]
        )

        link_type = None
        try:
            link_type = page.get_metadata("type", strategy=["og"]).split(".")[0]
        except Exception:
            link_type = "website"

        image = page.get_metadata("image", strategy=["og", "dc", "meta"])

        data = {
            "title": title,
            "short_description": description,
            "image": image,
            "link_type": link_type,
        }

    return {k: v for k, v in data.items() if v is not None}


def link_create(*, url: str, user: settings.AUTH_USER_MODEL) -> Link:
    page_data = get_url_data(url=url)

    link = Link(url=url, user=user, **page_data)
    link.full_clean()
    link.save()

    return link


def link_delete(*, link: Link):
    link.delete()


@transaction.atomic
def link_update(*, link: Link, data) -> Link:
    pass
