# Generated by Django 5.1 on 2024-08-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaspi', '0002_rename_goods_good_rename_magazinesgoods_magazinegood_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazine',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
