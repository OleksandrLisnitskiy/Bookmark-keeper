# Generated by Django 4.1.4 on 2022-12-27 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmarks', '0002_alter_groups_options_alter_tasks_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groups',
            options={'ordering': ['creation_date'], 'verbose_name': 'Group'},
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['creation_date'], 'verbose_name': 'Task'},
        ),
    ]
