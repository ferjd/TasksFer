# Generated by Django 4.2.1 on 2023-05-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_completed_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='importance',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
        migrations.AddField(
            model_name='task',
            name='observations',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='task',
            name='urgency',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1),
        ),
    ]