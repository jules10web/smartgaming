# Generated by Django 5.0 on 2023-12-23 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_room_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='image_url',
            new_name='image',
        ),
    ]
