from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PENDING = 'Pendiente'
    TODO = 'Por hacer'
    ASSIGNED = 'Asignada'
    IN_PROGRESS = 'En curso'
    DELAYED = 'Demorada'
    COMPLETED = 'Finalizada'
    
    STATUS_CHOICES = [
        (PENDING, 'Pendiente'),
        (TODO, 'Por hacer'),
        (ASSIGNED, 'Asignada'),
        (IN_PROGRESS, 'En curso'),
        (DELAYED, 'Demorada'),
        (COMPLETED, 'Finalizada'),
    ]

    PRIORITY_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    delegated_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='delegated_tasks')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    importance = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    urgency = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    observations = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title