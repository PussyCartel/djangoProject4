# Generated by Django 3.2.3 on 2021-05-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_attestation_variables'),
    ]

    operations = [
        migrations.AddField(
            model_name='attestation',
            name='articel',
            field=models.CharField(max_length=255, null=True, verbose_name='Анкета'),
        ),
        migrations.AddField(
            model_name='attestation',
            name='decode',
            field=models.CharField(max_length=255, null=True, verbose_name='Расшифровка параметра'),
        ),
        migrations.AddField(
            model_name='attestation',
            name='mark',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='attestation',
            name='source',
            field=models.CharField(max_length=255, null=True, verbose_name='Источник'),
        ),
        migrations.AddField(
            model_name='attestation',
            name='variable_meaning',
            field=models.CharField(max_length=255, null=True, verbose_name='Значение переменной'),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]