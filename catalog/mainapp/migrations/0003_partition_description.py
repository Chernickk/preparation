# Generated by Django 3.2.9 on 2021-11-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_partition'),
    ]

    operations = [
        migrations.AddField(
            model_name='partition',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
