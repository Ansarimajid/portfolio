# Generated by Django 4.2.4 on 2023-09-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_alter_websitesetting_map_iframe'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesetting',
            name='slider_particle_is_active',
            field=models.BooleanField(default=True),
        ),
    ]