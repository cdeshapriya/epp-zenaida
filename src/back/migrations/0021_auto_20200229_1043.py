# Generated by Django 2.2.10 on 2020-02-29 10:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0020_auto_20200226_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_fax',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Fax'),
        ),
    ]