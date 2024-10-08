# Generated by Django 5.1 on 2024-09-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_catalog", "0003_alter_product_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(auto_now_add=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateField(
                auto_now=True, verbose_name="Дата последнего изменения"
            ),
        ),
    ]
