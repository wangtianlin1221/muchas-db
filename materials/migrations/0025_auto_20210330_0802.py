# Generated by Django 3.0.7 on 2021-03-30 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0024_auto_20210327_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='subset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curves', to='materials.Subset'),
        ),
    ]
