# Generated by Django 2.1 on 2018-08-31 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0002_auto_20180829_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditionrecord',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
