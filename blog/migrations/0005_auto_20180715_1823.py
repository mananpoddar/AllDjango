# Generated by Django 2.0 on 2018-07-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180714_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='time',
            field=models.TimeField(),
        ),
    ]
