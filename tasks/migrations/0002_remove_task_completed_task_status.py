# Generated by Django 4.2.1 on 2023-05-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Por hacer', 'Por hacer'), ('Asignada', 'Asignada'), ('En curso', 'En curso'), ('Demorada', 'Demorada'), ('Finalizada', 'Finalizada')], default='Pendiente', max_length=20),
        ),
    ]
