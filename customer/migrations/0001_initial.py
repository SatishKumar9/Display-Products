# Generated by Django 2.1.3 on 2018-11-17 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(null=True)),
                ('Customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cus', to=settings.AUTH_USER_MODEL)),
                ('prod', models.ManyToManyField(blank=True, to='vendor.Product')),
            ],
        ),
    ]
