# Generated by Django 5.1.3 on 2024-12-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Base_App", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemlist",
            name="Category_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="items",
            name="Item_name",
            field=models.CharField(max_length=50),
        ),
    ]
