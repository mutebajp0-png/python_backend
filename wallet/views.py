from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin

from .models import Wallet
from .serializers import WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):

    serializer_class = WalletSerializer
    permission_classes = [
    IsAdmin,
]

    def get_queryset(self):

        user = self.request.user

        # administrateur → voit tous ses départements
        if user.role == "admin":
            return Wallet.objects.filter(owner=user)

        # manager → voit uniquement son département
        return Wallet.objects.filter(manager=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    