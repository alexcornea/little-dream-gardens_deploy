# Generated by Django 3.0.4 on 2020-12-28 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20201228_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='diy',
        ),
        migrations.RemoveField(
            model_name='post',
            name='gardens',
        ),
        migrations.RemoveField(
            model_name='post',
            name='getting_started',
        ),
        migrations.RemoveField(
            model_name='post',
            name='terrariums',
        ),
        migrations.AddField(
            model_name='gettingstarted',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Post'),
        ),
    ]