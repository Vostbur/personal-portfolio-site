# Generated by Django 3.2.3 on 2021-05-22 19:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
