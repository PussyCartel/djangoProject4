# Generated by Django 3.2.3 on 2021-05-14 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_attestation'),
    ]

    operations = [
        migrations.AddField(
            model_name='attestation',
            name='variables',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.var', verbose_name='переменные'),
        ),
    ]
