from rest_framework import serializers
from .models import Contacts, ContactsList

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = [
            "id",
            "name",
            "email",
            "telephone",
            "date_register",
            "account",
        ]

        read_only_fields = ["id", "account"]

    def create(self, validated_data):
        return Contacts.objects.create(**validated_data)


class ContactsListSerializer(serializers.Serializer):
    class Meta:
        model = ContactsList
        fields = [
            "contact",
            "account",
            "id",
        ]

        read_only_fields = ["contact", "account", "id"]

        def create(self, validated_data):
            contact = ContactsList.objects.create(**validated_data)
            return contact