from django.db import models


class Product(models.Model):
    """
    Таблица товаров.
    """

    product_name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        verbose_name="картинка",
        upload_to="product_catalog/photo",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")
    is_active = models.BooleanField(default=True, verbose_name="Статус")

    def __str__(self):
        return f"{self.product_name} ({self.description})"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("id",)


class Category(models.Model):
    """
    Таблица категорий.
    """

    category_name = models.CharField(max_length=100, verbose_name="категория")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
