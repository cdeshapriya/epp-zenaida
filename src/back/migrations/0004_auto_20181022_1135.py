# Generated by Django 2.1.2 on 2018-10-22 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_auto_20181022_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'base_manager_name': 'contacts', 'default_manager_name': 'contacts'},
        ),
    ]
