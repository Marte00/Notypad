# Generated by Django 4.1.7 on 2023-03-03 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_folder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Folder',
        ),
    ]
