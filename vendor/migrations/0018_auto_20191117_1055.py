# Generated by Django 2.2.5 on 2019-11-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0017_auto_20191117_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_pic',
            field=models.ImageField(blank=True, upload_to='static/vendor/images'),
        ),
    ]