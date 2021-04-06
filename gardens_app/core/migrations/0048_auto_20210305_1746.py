# Generated by Django 3.0.4 on 2021-03-05 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20210304_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='core.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
