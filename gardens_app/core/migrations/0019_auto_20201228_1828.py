# Generated by Django 3.0.4 on 2020-12-28 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20201228_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='terrariums',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Terrariums'),
        ),
        migrations.AlterField(
            model_name='post',
            name='gardens',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Gardens'),
        ),
    ]
