from rest_framework import serializers


class OperationSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    type = serializers.CharField()

    wallet = serializers.CharField()

    title = serializers.CharField()

    description = serializers.CharField()

    amount = serializers.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    date = serializers.DateField()