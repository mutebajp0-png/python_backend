from rest_framework import serializers

from .models import Income


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income

        fields = [
            "id",
            "wallet",
            "title",
            "description",
            "amount",
            "date",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "created_at",
            "updated_at",
        ]