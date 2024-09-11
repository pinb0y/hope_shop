# Generated by Django 5.1 on 2024-09-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_catalog", "0007_product_standard"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="standard",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                unique=True,
                verbose_name="Стандарт на продукцию",
            ),
        ),
    ]
