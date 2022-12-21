from django.db import models
from django.contrib.auth.models import User

class ALLurl(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True)
    websitename = models.CharField(max_length=100, null= True, blank=True)
    url = models.URLField(max_length=1000, null= True, blank=False)
    shorted = models.CharField(max_length=50, null= True, blank=True)
