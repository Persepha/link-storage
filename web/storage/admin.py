from django.contrib import admin

from storage.models.collection import Collection
from storage.models.link import Link


@admin.register(Link)
class LinkItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Collection)
class CollectionItemAdmin(admin.ModelAdmin):
    pass