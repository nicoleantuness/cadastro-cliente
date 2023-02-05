from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "id",
            "name",
            "email",
            "telephone",
            "date_register",
        ]
        read_only_fields = ["id"]
        
    def create(self, validated_data):
        return Account.objects.create(**validated_data)
    