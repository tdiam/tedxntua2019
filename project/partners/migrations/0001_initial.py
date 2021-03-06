# Generated by Django 2.1.3 on 2018-11-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('partner_type', models.CharField(choices=[('GSP', 'Grand Sponsors Plus'), ('GS', 'Grand Sponsors'), ('SPO', 'Sponsors'), ('SUP', 'Supporters'), ('MP', 'Media Partners'), ('CP', 'Community Partners')], max_length=3)),
                ('link', models.URLField()),
            ],
        ),
    ]
