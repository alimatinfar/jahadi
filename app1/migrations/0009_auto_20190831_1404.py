# Generated by Django 2.2.1 on 2019-08-31 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20190831_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farakhan',
            name='present_profile',
        ),
        migrations.RemoveField(
            model_name='farakhan',
            name='ready_profile',
        ),
        migrations.CreateModel(
            name='Profile_ready',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_farakhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Farakhan')),
                ('id_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Profile_present',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_farakhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Farakhan')),
                ('id_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Profile')),
            ],
        ),
    ]