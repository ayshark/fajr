# Generated by Django 4.1.4 on 2022-12-26 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
