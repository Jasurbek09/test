# Generated by Django 3.2.5 on 2021-07-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210715_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='title',
            field=models.CharField(default='title', max_length=200),
        ),
    ]