# Generated by Django 3.0.5 on 2020-04-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FilePathField(path='/Users/miklos/Desktop/Files/Personal/Programming Competitions/HackDSC 2020/party_app/mysite/static/myapi'),
        ),
    ]
