# Generated by Django 2.2.6 on 2019-11-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint_backlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint_backlog_item',
            name='owner',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
