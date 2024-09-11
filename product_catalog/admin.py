from django.contrib import admin
from product_catalog.models import Product, Category, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "product_name",
        "category",
        "image",
        "created_at",
        "updated_at",
    )
    list_filter = ("category",)
    search_fields = (
        "product_name",
        "description",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "category_name",
    )

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("product", "number", "name", "is_active")

