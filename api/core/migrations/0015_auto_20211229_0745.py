# Generated by Django 3.2.9 on 2021-12-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20211226_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(blank=True, db_column='OrderDate', default='2021-12-29'),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2021-12-29'),
        ),
    ]
