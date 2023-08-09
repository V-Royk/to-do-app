from django.db import models
from django.utils.timezone import now

# Create your models here.

class Task(models.Model):
    title = models.TextField(null=False, max_length=20)
    is_done = models.BooleanField(default=False)
    done_date = models.DateTimeField(null=True)
    create_at = models.DateTimeField(default=now)
    update_at = models.DateTimeField(null=True)
    description = models.TextField(max_length=500, null=True)


    def __str__(self):
        return self.title
    
    


