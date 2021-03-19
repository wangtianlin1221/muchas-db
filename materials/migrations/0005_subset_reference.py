# Generated by Django 3.0.7 on 2021-03-10 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_remove_computationaldetails_external_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='subset',
            name='reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subsets', to='materials.Reference'),
        ),
    ]