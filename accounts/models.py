from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telephone = models.IntegerField()
    date_register = models.DateTimeField()

