# Generated by Django 4.0.3 on 2023-02-07 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_ststus_category_status_remove_product_ststus_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='cat_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='prod_image',
        ),
    ]
