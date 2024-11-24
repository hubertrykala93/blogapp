from django.contrib import admin
from .models import Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = [
        "id",
        "formatted_created_at",
        "formatted_updated_at",
        "user",
        "title",
        "content",
        "slug",
    ]
    exclude = ["slug"]

    def formatted_created_at(self, obj):
        if obj.created_at:
            return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"

    def formatted_updated_at(self, obj):
        if obj.updated_at:
            return obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    formatted_updated_at.short_description = "Created At"
