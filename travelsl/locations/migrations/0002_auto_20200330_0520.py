# Generated by Django 3.0.4 on 2020-03-30 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'ordering': ['url']},
        ),
    ]
