
from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.CharField(max_length=200, verbose_name="Слаг", default="#")
    body = models.TextField(verbose_name="Содержание")
    preview = models.ImageField(upload_to="blog/preview", blank=True, null=True, verbose_name="Превью")
    created_at = models.DateField(verbose_name="Дата создания", default=timezone.now)
    is_published = models.BooleanField(verbose_name="Статус публикации")
    views_count = models.IntegerField(verbose_name="Счетчик просмотров", default=0)

