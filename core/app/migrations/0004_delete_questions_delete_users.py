# Generated by Django 5.1.1 on 2024-09-25 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
