from django.db import models

class Contacts(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telephone = models.IntegerField()
    date_register = models.DateTimeField()

    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='created_contact'
    )