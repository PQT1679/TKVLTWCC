# Generated by Django 3.1.4 on 2022-02-25 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20220109_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(blank=True, db_column='OrderDate', default='2022-02-25'),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2022-02-25'),
        ),
    ]
