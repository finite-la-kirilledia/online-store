# Generated by Django 2.0.5 on 2018-05-17 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='updated_date',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='orderline',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='orderline',
            old_name='updated_date',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='orderstatus',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='orderstatus',
            old_name='updated_date',
            new_name='updated',
        ),
    ]