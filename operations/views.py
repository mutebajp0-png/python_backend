from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from itertools import chain

from expenses.models import Expense
from incomes.models import Income

class OperationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role == 'admin':
            expenses = Expense.objects.all()
            incomes = Income.objects.all()
        else:
            expenses = Expense.objects.filter(wallet__manager=user)
            incomes = Income.objects.filter(wallet__manager=user)

        operations = []

        for expense in expenses:
            operations.append({
                'id': str(expense.id),
                'wallet': str(expense.wallet.id),
                'title': expense.title,
                'subtitle': 'En attente • ' + expense.date.strftime('%H:%M'),
                'description': expense.description or '',
                'motif': getattr(expense, 'motif', ''),
                'dateTime': expense.date.isoformat() + 'T00:00:00',  # DateTime au format ISO
                'amount': float(expense.amount),
                'positive': False,
                'badge': 'En attente',
                'color': '#FF8A00',
                'icon': 0xe316,  # IconData codePoint pour Icons.arrow_upward_rounded
                'currency': expense.wallet.currency.lower(),
                'category': getattr(expense, 'category', None),
                'attachmentsAllowed': getattr(expense, 'attachments_allowed', True),
                'attachments': [],  # Implémente si tu gères réellement les pièces jointes
                'type': 'expense',
            })

        for income in incomes:
            operations.append({
                'id': str(income.id),
                'wallet': str(income.wallet.id),
                'title': income.title,
                'subtitle': 'Approuvé • ' + income.date.strftime('%H:%M'),
                'description': income.description or '',
                'motif': getattr(income, 'motif', ''),
                'dateTime': income.date.isoformat() + 'T00:00:00',
                'amount': float(income.amount),
                'positive': True,
                'badge': 'Approuvé',
                'color': '#00B86B',
                'icon': 0xe313,  # IconData codePoint pour Icons.arrow_downward_rounded
                'currency': income.wallet.currency.lower(),
                'category': getattr(income, 'category', None),
                'attachmentsAllowed': getattr(income, 'attachments_allowed', True),
                'attachments': [],
                'type': 'income',
            })

        operations.sort(key=lambda op: op['dateTime'], reverse=True)

        return Response(operations)
