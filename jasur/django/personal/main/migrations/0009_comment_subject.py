# Generated by Django 3.2.5 on 2021-07-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210717_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
