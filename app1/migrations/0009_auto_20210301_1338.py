# Generated by Django 3.1.3 on 2021-03-01 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20210227_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='Bills_id',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
