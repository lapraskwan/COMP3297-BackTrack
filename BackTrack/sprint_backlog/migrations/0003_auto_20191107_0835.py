# Generated by Django 2.2.6 on 2019-11-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint_backlog', '0002_auto_20191107_0556'),
    ]

    operations = [
        migrations.CreateModel(
            name='capacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(default=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='sprint_backlog_item',
            options={'ordering': ['PBI', 'estimation']},
        ),
    ]
