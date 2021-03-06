# Generated by Django 2.0.5 on 2018-05-21 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_auto_20180520_1915'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0008_auto_20180521_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderelement',
            old_name='price_per_item',
            new_name='price',
        ),
        migrations.AddField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='basketelement',
            name='basket',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Basket'),
        ),
        migrations.AddField(
            model_name='basketelement',
            name='book',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
        migrations.AddField(
            model_name='basketelement',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basketelement',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='basketelement',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
