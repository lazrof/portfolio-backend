# Generated by Django 3.0 on 2020-05-06 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translatable_content', '0002_auto_20200506_0124'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contents',
            new_name='Content',
        ),
    ]
