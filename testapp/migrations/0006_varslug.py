# Generated by Django 3.2.3 on 2021-05-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20210514_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='VarSlug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='Уникальный идентификатор для цитирования')),
            ],
        ),
    ]
