# Generated by Django 3.1.3 on 2021-01-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_blog_type_of'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
