from itertools import chain

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from expenses.models import Expense
from incomes.models import Income


class OperationView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):

        user = request.user

        if user.role == "admin":

            expenses = Expense.objects.all()

            incomes = Income.objects.all()

        else:

            expenses = Expense.objects.filter(
                wallet__manager=user
            )

            incomes = Income.objects.filter(
                wallet__manager=user
            )

        operations = []

        for expense in expenses:

            operations.append({

                "id": expense.id,

                "type": "expense",

                "wallet": expense.wallet.name,

                "title": expense.title,

                "description": expense.description,

                "amount": expense.amount,

                "date": expense.date,

            })

        for income in incomes:

            operations.append({

                "id": income.id,

                "type": "income",

                "wallet": income.wallet.name,

                "title": income.title,

                "description": income.description,

                "amount": income.amount,

                "date": income.date,

            })

        operations.sort(
            key=lambda x: x["date"],
            reverse=True,
        )

        return Response(operations)