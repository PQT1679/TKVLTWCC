# Generated by Django 3.2.9 on 2022-04-21 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20220420_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(db_column='OrderDate', default='2022-04-21'),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2022-04-21'),
        ),
    ]
