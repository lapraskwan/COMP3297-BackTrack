# Generated by Django 2.2.6 on 2019-11-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint_backlog', '0006_auto_20191110_1335'),
    ]

    operations = [
        migrations.DeleteModel(
            name='capacity',
        ),
        migrations.AlterField(
            model_name='sprint_backlog_item',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Finished', 'Finished'), ('Unfinished', 'Unfinished')], default='Pending', max_length=100),
        ),
    ]
