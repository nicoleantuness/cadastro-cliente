from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "name",
            "email",
            "telephone",
            "date_register",
        ]

    def create(self, validated_data):
        return Account.objects.create(**validated_data)