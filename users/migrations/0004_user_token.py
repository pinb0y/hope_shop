# Generated by Django 4.2 on 2024-09-22 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_country_alter_user_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Токен"
            ),
        ),
    ]
