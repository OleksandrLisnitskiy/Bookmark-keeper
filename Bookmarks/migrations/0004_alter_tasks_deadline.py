# Generated by Django 4.1.4 on 2022-12-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmarks', '0003_alter_groups_options_alter_tasks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='deadline',
            field=models.DateTimeField(default=None, help_text='Deadline of this task, not obligatory, default null', null=True),
        ),
    ]
