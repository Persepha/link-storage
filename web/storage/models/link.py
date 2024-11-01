from django.conf import settings
from django.db import models

from common.models import BaseModel


class Link(BaseModel):
    LINK_TYPES = (
        ("website", "Website"),
        ("book", "Book"),
        ("article", "Article"),
        ("music", "Music"),
        ("video", "Video"),
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
    )
    short_description = models.TextField(blank=True)
    url = models.URLField(unique=True)
    image = models.URLField(blank=True)
    link_type = models.CharField(max_length=20, choices=LINK_TYPES, default="website")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="links",
    )

    def __str__(self):
        return self.title
