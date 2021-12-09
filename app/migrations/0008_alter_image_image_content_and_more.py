# Generated by Django 4.0 on 2021-12-09 02:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211207_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_content',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
