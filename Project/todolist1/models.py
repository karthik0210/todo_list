

# from django.db import models

# class Task(models.Model):
#     PENDING = 'pending'
#     COMPLETED = 'completed'
    
#     STATUS_CHOICES = [
#         (PENDING, 'Pending'),
#         (COMPLETED, 'Completed'),
#     ]
    
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     due_date = models.DateField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

#     def __str__(self):
#         return self.name

from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# from django.db import models
# from django.utils import timezone

# class Task(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     status = models.CharField(max_length=50, choices=[
#         ('Pending', 'Pending'),
#         ('Completed', 'Completed'),
#         ('In Progress', 'In Progress')
#     ])
#     due_date = models.DateTimeField(null=True, blank=True)
#     created_at = models.DateTimeField(default=timezone.now, editable=False)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.created_at = timezone.now()
#         return super(Task, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name





