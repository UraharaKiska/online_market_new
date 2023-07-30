# Generated by Django 4.2.3 on 2023-07-26 06:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photo_user/%Y/%m/%d', verbose_name='photo'),
        ),
    ]