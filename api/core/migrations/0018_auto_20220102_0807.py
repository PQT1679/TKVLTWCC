# Generated by Django 3.2.9 on 2022-01-02 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20211231_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(blank=True, db_column='OrderDate', default='2022-01-02'),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2022-01-02'),
        ),
    ]
