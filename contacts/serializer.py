from rest_framework import serializers
from .models import Contacts

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = [
            "name",
            "email",
            "telephone",
            "date_register",
        ]

        read_only_fields = ["account"]

    def create(self, validated_data):
        return Contacts.objects.create(**validated_data)