# Generated by Django 3.0.4 on 2020-04-25 09:59

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_triprequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='image',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]