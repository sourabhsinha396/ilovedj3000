# Generated by Django 3.1.3 on 2020-11-14 04:22

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_free', models.BooleanField(default=False)),
                ('price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blogs.blog')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
