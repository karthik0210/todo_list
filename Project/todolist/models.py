# models.py

from django.db import models

class Task(models.Model):
    PENDING = 'pending'
    COMPLETED = 'completed'
    
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return self.name
