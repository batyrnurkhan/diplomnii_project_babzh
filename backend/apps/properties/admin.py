from django.contrib import admin

from .models import Property, PropertyViews


class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "country", "subject", "subject_type"]
    list_filter = ["subject", "subject_type", "country"]


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyViews)
