# Generated by Django 3.0.4 on 2020-12-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_category_kind'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='kind',
        ),
        migrations.AddField(
            model_name='post',
            name='kind',
            field=models.CharField(choices=[('GS', 'Getting Started'), ('DIY', 'DIY'), ('GR', 'Gardens'), ('TR', 'Terrariums')], default=' ', max_length=3),
        ),
    ]
