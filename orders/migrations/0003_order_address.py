# Generated by Django 2.0.5 on 2018-05-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180516_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=225, null=True),
        ),
    ]
