# Generated by Django 2.1 on 2018-10-10 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_customfields'),
    ]

    operations = [
        migrations.AddField(
            model_name='customfields',
            name='date_column',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='customfields',
            name='date_column2',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
