# Generated by Django 5.0.6 on 2024-06-01 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautiful_chat', '0005_userprofile_delete_profilepictures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='pic_hash',
        ),
    ]
