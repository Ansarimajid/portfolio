# Generated by Django 4.2.4 on 2023-09-03 18:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_alter_headerfootersetting_footer_col1_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerfootersetting',
            name='footer_col1_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='headerfootersetting',
            name='quick_link_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
