# Generated by Django 2.2.3 on 2019-09-11 13:11
import jdatetime
from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='datetime',
            field=django_jalali.db.models.jDateTimeField(default=jdatetime.date(1390, 2, 3)),
            preserve_default=False,
        ),
    ]
