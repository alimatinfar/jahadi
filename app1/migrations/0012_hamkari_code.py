# Generated by Django 2.2.1 on 2019-09-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20190906_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hamkari_code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_code', models.CharField(max_length=200)),
                ('darman', models.BooleanField()),
                ('sakht', models.BooleanField()),
                ('amoozesh', models.BooleanField()),
                ('farhangi', models.BooleanField()),
                ('daroo', models.BooleanField()),
                ('lebas', models.BooleanField()),
                ('ghaza', models.BooleanField()),
                ('tahrir', models.BooleanField()),
                ('masaleh', models.BooleanField()),
                ('naghdi_mostaghim', models.BooleanField()),
                ('naghdi_ghest', models.BooleanField()),
            ],
        ),
    ]
