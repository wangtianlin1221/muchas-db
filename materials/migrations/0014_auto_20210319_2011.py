# Generated by Django 3.0.7 on 2021-03-20 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0013_auto_20210319_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shannonionicradii',
            name='key',
        ),
        migrations.AlterField(
            model_name='shannonionicradii',
            name='charge',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shannonionicradiiref',
            name='charge',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
