# Generated by Django 3.2.3 on 2021-05-14 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_varoption'),
    ]

    operations = [
        migrations.AddField(
            model_name='var',
            name='VarMean',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testapp.varoption'),
        ),
    ]
