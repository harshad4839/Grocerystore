# Generated by Django 3.1.2 on 2021-06-25 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Owner', '0005_auto_20210625_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='expires',
            field=models.DateField(null=True),
        ),
    ]
