# Generated by Django 5.0 on 2023-12-04 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 19, 14, 0, 84549, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicación'),
        ),
    ]
