# Generated by Django 2.0.5 on 2018-05-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20180517_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookstatus',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=225, null=True),
        ),
    ]
