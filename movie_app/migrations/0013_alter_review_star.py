# Generated by Django 4.1.1 on 2022-09-24 10:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_remove_movie_rai_review_star_delete_raiting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
