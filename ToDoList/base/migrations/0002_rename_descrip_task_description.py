# Generated by Django 4.2.4 on 2023-09-03 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descrip',
            new_name='description',
        ),
    ]
