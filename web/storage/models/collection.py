from django.db import models
from django.conf import settings

from common.models import BaseModel
from storage.models.link import Link


class Collection(BaseModel):
    name = models.CharField(
        db_index=True,
        max_length=255,
    )
    short_description = models.TextField(blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Collections",
    )

    links = models.ManyToManyField(
        Link,
        blank=True,
    )

    def __str__(self):
        return self.name
