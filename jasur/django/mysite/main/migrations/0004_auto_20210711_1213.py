# Generated by Django 3.2.5 on 2021-07-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_country_desk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chelsea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100)),
                ('best_player', models.CharField(max_length=100)),
                ('golkiper', models.CharField(max_length=100)),
                ('coach', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='logo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload'),
        ),
    ]
