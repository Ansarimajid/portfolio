# Generated by Django 4.2.4 on 2023-10-18 05:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='policy_texts',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='terms',
            name='term_texts',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]