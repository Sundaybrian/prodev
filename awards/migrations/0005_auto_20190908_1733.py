# Generated by Django 2.2.4 on 2019-09-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_auto_20190908_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='creativity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='design',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='mobile',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='usability',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
