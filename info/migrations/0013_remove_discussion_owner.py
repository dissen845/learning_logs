# Generated by Django 3.2.9 on 2021-11-17 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0012_auto_20211117_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='owner',
        ),
    ]