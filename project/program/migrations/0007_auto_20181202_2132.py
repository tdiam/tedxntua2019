# Generated by Django 2.1.3 on 2018-12-02 21:32

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_auto_20181202_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, height_field='image_height', null=True, upload_to='static/', verbose_name='Image', width_field='image_width'),
        ),
    ]
