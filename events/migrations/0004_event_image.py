# Generated by Django 2.1.7 on 2019-05-29 12:39

from django.db import migrations, models
import iqbusiness.utils


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventform'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=iqbusiness.utils.RandomFileName('Event')),
        ),
    ]