
from django.db import models
from django.utils import timezone

#model for managing each task.

class Task(models.Model):

    #predefined choices for status
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True) 

    #soft deleting the object without deleting from database.
    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    #setting deleted_at as None to restoring the object
    def restore(self):
        self.deleted_at = None
        self.save()

    def __str__(self):
        return self.title
