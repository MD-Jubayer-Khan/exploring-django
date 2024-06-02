# Generated by Django 4.2.13 on 2024-06-02 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='album_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='album_release_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
