# Generated by Django 3.2.4 on 2021-06-30 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndWiki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='peoples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='recaps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
