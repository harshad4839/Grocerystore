# Generated by Django 3.2.4 on 2021-06-24 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0002_auto_20210624_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='expirarydate',
        ),
    ]
