from django.contrib import admin

from . import models

@admin.register(models.Center)
class CenterAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'address',
        'code',
        'homepage',
        'telephone',
    )

    list_display_links = (
        'name',
    )

@admin.register(models.CenterUser)
class CenterUserAdmin(admin.ModelAdmin):

    list_display = (
        'center_id',
        'username',
    )

    list_display_links = (
        'center_id',
        'username',
    )