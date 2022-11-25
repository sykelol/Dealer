from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dealer(models.Model):
    dealer = models.CharField(max_length = 100)
    #financing = 
    #status = 
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.dealer