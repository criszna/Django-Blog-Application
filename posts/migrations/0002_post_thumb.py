# Generated by Django 3.1.2 on 2020-10-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
