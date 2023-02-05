from django.db import models
import uuid

class Contacts(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telephone = models.IntegerField()
    date_register = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='contacts'
    )

    list = models.ManyToManyField(
        "accounts.Account",
        through="contacts.ContactsList",
        related_name="account"
    )

class ContactsList(models.Model):
    contact = models.ForeignKey(
        "contacts.Contacts",
        on_delete=models.CASCADE,
        related_name="contact_list"
    )

    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="account_contact_list"
    )