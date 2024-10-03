from django.core.cache import cache

from config.settings import CACHE_ENABLED
from product_catalog.models import Category


def get_cashed_categories():
    """
    Возвращает список категорий из кеша или из БД если кеша нет
    """
    categories = Category.objects.all()
    if not CACHE_ENABLED:
        return categories

    key = "category_list"
    cached_categories = cache.get(key)

    if cached_categories is not None:
        return cached_categories

    cache.set(key, categories)
    return categories
