# Generated by Django 3.2.3 on 2021-05-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_alter_var_meaningtoattestation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attestation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
