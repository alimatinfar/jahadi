# Generated by Django 2.2.3 on 2019-09-13 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_auto_20190913_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farakhan',
            name='hamkari_type',
            field=models.CharField(choices=[('n', 'نقدی'), ('k', 'خدماتی'), ('e', 'اجناس اهدایی')], max_length=1, verbose_name='نوع همکاری'),
        ),
    ]
