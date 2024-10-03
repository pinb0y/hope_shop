from django.core.cache import cache

from config.settings import CACHE_ENABLED
from product_catalog.models import Category


def get_cashed_categories(category_pk):
    if CACHE_ENABLED:
        key = f"category_list_{category_pk}"
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()

    return category_list
