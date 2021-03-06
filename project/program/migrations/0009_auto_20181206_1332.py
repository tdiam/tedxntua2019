# Generated by Django 2.1.2 on 2018-12-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0008_auto_20181206_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image_height',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='image_width',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='presenter',
            name='image_height',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='presenter',
            name='image_width',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]
