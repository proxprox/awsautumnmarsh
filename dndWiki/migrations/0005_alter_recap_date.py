# Generated by Django 3.2.4 on 2021-06-30 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dndWiki', '0004_auto_20210629_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recap',
            name='date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
