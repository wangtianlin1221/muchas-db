# Generated by Django 3.0.7 on 2021-04-08 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0030_auto_20210407_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='created',
        ),
        migrations.RemoveField(
            model_name='author',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='author',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='author',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='created',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='updated_by',
        ),
    ]