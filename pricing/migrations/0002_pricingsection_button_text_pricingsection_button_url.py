# Generated by Django 4.2.4 on 2023-09-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingsection',
            name='button_text',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pricingsection',
            name='button_url',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
