# Generated by Django 4.2.9 on 2024-01-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialnetwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_liked',
            field=models.TextField(null=True),
        ),
    ]
