# Generated by Django 4.1.1 on 2022-09-25 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0014_alter_movie_rev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='rev',
            new_name='reviews',
        ),
    ]
