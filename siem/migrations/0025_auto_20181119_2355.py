# Generated by Django 2.0.4 on 2018-11-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0024_auto_20180427_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logevent',
            name='eol_date_backup',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterField(
            model_name='logevent',
            name='eol_date_local',
            field=models.DateField(db_index=True),
        ),
    ]