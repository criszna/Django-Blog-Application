# Generated by Django 3.1.2 on 2020-10-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_savepost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savepost',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
