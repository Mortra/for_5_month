# Generated by Django 4.1.1 on 2022-09-25 13:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0018_alter_review_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
