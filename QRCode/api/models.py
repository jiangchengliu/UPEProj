from django.db import models

class CustomUser(models.Model):
    name = models.CharField(max_length=255)
