# Generated by Django 3.0.4 on 2021-01-03 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20201230_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='kind',
            field=models.CharField(choices=[('Getting Started', 'Getting Started'), ('DIY', 'DIY'), ('GR', 'Gardens'), ('TR', 'Terrariums')], default=' ', max_length=20),
        ),
    ]
