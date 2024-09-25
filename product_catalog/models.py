from django.db import models

from users.models import User


class Product(models.Model):
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
    owner = models.ForeignKey(User, null=True, blank=True, verbose_name="Владелец", on_delete=models.SET_NULL)
    price = models.IntegerField(verbose_name="цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")
    is_published = models.BooleanField(default=False, verbose_name="Статус публикации")

    def __str__(self):
        return f"{self.product_name} ({self.description})"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("id",)
        permissions = [
            ("set_published", "Can publish products"),
            ("change_description", "Can change description"),
            ("change_category", "Can change category"),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    number = models.IntegerField(verbose_name="Номер версии")
    name = models.CharField(max_length=100, verbose_name="Название версии")
    is_active = models.BooleanField(verbose_name="Признак текущей версии")

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        constraints = [
            models.UniqueConstraint(fields=["product", "number"],
                                    name='unique_versions',
                                    violation_error_message="Номер версии должен быть уникальным")
        ]

    def __str__(self):
        return f"{self.number} - {self.name}"


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
