# Generated by Django 3.0.4 on 2020-12-30 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20201230_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category2',
        ),
    ]