# Generated by Django 2.1.2 on 2018-11-13 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='first',
            field=models.CharField(max_length=255, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='last',
            field=models.CharField(max_length=255, verbose_name='Last name'),
        ),
    ]
