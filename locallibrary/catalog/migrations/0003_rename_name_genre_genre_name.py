# Generated by Django 4.2.8 on 2023-12-18 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='genre_name',
        ),
    ]