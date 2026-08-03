from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Income
from .serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):

    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        # administrateur
        if user.role == "admin":
            return Income.objects.all()

        # manager
        return Income.objects.filter(
            wallet__manager=user
        )

    def perform_create(self, serializer):

        wallet = serializer.validated_data["wallet"]

        user = self.request.user

        # empêcher un manager d'enregistrer une entrée
        # dans le département d'un autre manager
        if user.role == "manager":

            if wallet.manager != user:

                raise PermissionError(
                    "Vous ne pouvez pas enregistrer une entrée dans ce département."
                )

        serializer.save(
            created_by=user
        )