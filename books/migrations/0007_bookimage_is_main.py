# Generated by Django 2.0.5 on 2018-05-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20180516_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
