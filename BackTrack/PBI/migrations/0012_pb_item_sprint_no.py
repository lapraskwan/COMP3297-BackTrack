# Generated by Django 2.2.6 on 2019-11-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PBI', '0011_auto_20191111_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='pb_item',
            name='sprint_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
