from django.contrib import admin

from product_blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
        "preview",
        "is_published",
        "created_at",
        "views_count",
    )
