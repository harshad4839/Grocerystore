# Generated by Django 3.2.5 on 2021-07-09 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0009_auto_20210709_0610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='createdat',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='updatedat',
            new_name='updated_at',
        ),
    ]