# Generated by Django 3.0.6 on 2020-05-20 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_release_generated'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='paramsFilter',
            field=models.TextField(default='version'),
        ),
    ]
