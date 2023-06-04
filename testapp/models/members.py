from django.db import models
from django.utils import timezone

class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        #Member.objects.filter(date__lte=timezone.now()).order_by('updated_at')
        return self.name