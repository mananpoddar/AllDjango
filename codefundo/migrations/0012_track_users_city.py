# Generated by Django 2.1.1 on 2018-10-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codefundo', '0011_auto_20181018_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='track_users',
            name='city',
            field=models.TextField(default='asdf', max_length=10),
        ),
    ]
