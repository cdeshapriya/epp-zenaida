# Generated by Django 2.1.2 on 2018-10-22 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_auto_20181022_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'base_manager_name': 'profiles', 'default_manager_name': 'profiles'},
        ),
        migrations.AlterModelOptions(
            name='registrar',
            options={'base_manager_name': 'registrars', 'default_manager_name': 'registrars'},
        ),
        migrations.AlterModelOptions(
            name='zone',
            options={'base_manager_name': 'zones', 'default_manager_name': 'zones'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='epp_id',
            field=models.CharField(blank=True, default=True, max_length=32, unique=True),
        ),
    ]
