# Generated by Django 3.1.4 on 2022-03-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20220325_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='carttotal',
        ),
        migrations.AddField(
            model_name='cart',
            name='numofproducts',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.FloatField(db_column='Total', default=0.0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(db_column='OrderDate', default='2022-03-29'),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2022-03-29'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(db_column='IMG', max_length=200, upload_to=''),
        ),
    ]
