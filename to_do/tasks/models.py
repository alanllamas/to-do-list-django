
from django.db import models
from users.models import User


class Task(models.Model):
    name        = models.CharField(max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(max_length=300, blank=True)
    duration    = models.DecimalField(max_digits=3, decimal_places=0, blank=False, null=False)
    user        = models.ForeignKey('users.User', related_name='tasks', on_delete=models.CASCADE, null=False)
    PRIORITY_CHOICES = (
        ('4', 'Emergency'),
        ('3', 'High'),
        ('2', 'Medium'),
        ('1', 'Low'),
    )
    priority    = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default= '2',
    )
    dead_line    = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    done         = models.BooleanField(blank=False,default=False)


    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)