# Generated by Django 2.0.5 on 2018-05-17 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20180517_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookcategory',
            options={'verbose_name_plural': 'Book categories'},
        ),
        migrations.RenameField(
            model_name='book',
            old_name='book_status',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='bookcategory',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='books.BookCategory'),
        ),
    ]