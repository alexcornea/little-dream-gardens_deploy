# Generated by Django 3.0.4 on 2020-12-15 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201215_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='name',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]