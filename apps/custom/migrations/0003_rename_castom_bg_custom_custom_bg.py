# Generated by Django 3.2.9 on 2022-02-04 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_auto_20220130_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custom',
            old_name='castom_bg',
            new_name='custom_bg',
        ),
    ]
