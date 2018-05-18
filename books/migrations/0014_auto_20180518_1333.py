# Generated by Django 2.0.5 on 2018-05-18 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20180517_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Country'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.BookStatus'),
        ),
    ]