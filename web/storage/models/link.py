from common.models import BaseModel
from django.conf import settings
from django.db import models


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
    url = models.URLField()
    image = models.URLField(blank=True)
    link_type = models.CharField(max_length=20, choices=LINK_TYPES, default="website")

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="links",
    )

    class Meta:
        unique_together = ('url', 'user')  # Ensure unique link per user

    def __str__(self):
        return f"{self.id} - {self.title}"
