# Generated by Django 4.2.4 on 2023-10-18 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarymenu',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
