# Generated by Django 2.0.5 on 2018-05-16 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.AlterModelOptions(
            name='bookstatus',
            options={'verbose_name_plural': 'Book statuses'},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={},
        ),
    ]
