# Generated by Django 2.2.6 on 2019-12-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20191205_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
