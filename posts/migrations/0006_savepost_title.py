# Generated by Django 3.1.2 on 2020-10-18 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_savepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='savepost',
            name='title',
            field=models.CharField(default='title', max_length=100),
        ),
    ]