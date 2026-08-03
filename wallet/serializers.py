from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Wallet

User = get_user_model()


class WalletSerializer(serializers.ModelSerializer):

    manager_username = serializers.CharField(write_only=True)
    manager_password = serializers.CharField(write_only=True)
    manager_first_name = serializers.CharField(write_only=True)
    manager_last_name = serializers.CharField(write_only=True)

    class Meta:
        model = Wallet

        fields = [
            "id",
            "name",
            "description",
            "currency",
            "initial_balance",
            "current_balance",
            "color",
            "icon",
            "is_active",

            "manager_username",
            "manager_password",
            "manager_first_name",
            "manager_last_name",
        ]

        read_only_fields = [
            "current_balance",
        ]

    def create(self, validated_data):

        username = validated_data.pop("manager_username")
        password = validated_data.pop("manager_password")
        first_name = validated_data.pop("manager_first_name")
        last_name = validated_data.pop("manager_last_name")

        owner = self.context["request"].user

        manager = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role="manager",
        )

        wallet = Wallet.objects.create(
            owner=owner,
            manager=manager,
            current_balance=validated_data["initial_balance"],
            **validated_data,
        )

        return wallet