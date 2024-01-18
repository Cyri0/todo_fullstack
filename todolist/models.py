from django.db import models

# Create your models here.

class Task(models.Model):
    is_visible = models.BooleanField(default=True)
    text = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text