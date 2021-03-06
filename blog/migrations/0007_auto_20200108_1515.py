# Generated by Django 3.0.2 on 2020-01-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_clip_downloaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='accepted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='clip',
            name='rejected',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='clip',
            name='reviewed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
