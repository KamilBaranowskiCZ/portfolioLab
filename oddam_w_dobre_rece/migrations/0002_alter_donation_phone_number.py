# Generated by Django 4.0.4 on 2022-05-19 13:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddam_w_dobre_rece', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^(?:\\(?\\?)?(?:[-\\.\\(\\)\\s]*(\\d)){9}\\)?$')]),
        ),
    ]
