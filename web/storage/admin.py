from django.contrib import admin

from storage.models.link import Link


@admin.register(Link)
class LinkItemAdmin(admin.ModelAdmin):
    pass
