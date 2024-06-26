# Generated by Django 5.0.6 on 2024-06-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautiful_chat', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('hash', models.CharField(max_length=200)),
                ('image', models.BinaryField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
