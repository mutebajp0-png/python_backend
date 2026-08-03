from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Expense
from .serializers import ExpenseSerializer
from accounts.permissions import IsAdminOrManager


class ExpenseViewSet(viewsets.ModelViewSet):

    serializer_class = ExpenseSerializer
    permission_classes = [
    IsAdminOrManager,
]

    def get_queryset(self):

        user = self.request.user

        if user.role == "admin":
            return Expense.objects.all()

        return Expense.objects.filter(
            wallet__manager=user
        )

    def perform_create(self, serializer):

        serializer.save(
            created_by=self.request.user
        )