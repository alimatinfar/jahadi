# Generated by Django 2.2.3 on 2019-09-18 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_auto_20190913_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='marital',
            field=models.CharField(choices=[('m', 'متاهل'), ('s', 'مجرد')], default=1, max_length=1, verbose_name='وضعیت تاهل'),
            preserve_default=False,
        ),
    ]
