# Generated by Django 2.2.4 on 2019-09-08 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0002_auto_20190908_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='profile',
        ),
        migrations.AddField(
            model_name='review',
            name='judge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
