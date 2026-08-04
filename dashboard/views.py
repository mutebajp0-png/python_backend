from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, Count
from wallet.models import Wallet
from incomes.models import Income
from expenses.models import Expense
from operations.models import Operation  # si tu utilises ce modèle pour mouvements
# from documents.models import Document

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_data(request):
    user = request.user

    # Filtrage des wallets selon rôle (exemple simple)
    if user.role == 'admin':
        wallets = Wallet.objects.filter(owner=user)
    else:
        wallets = Wallet.objects.filter(manager=user)

    # Calculs globaux
    total_treasury = wallets.aggregate(Sum('current_balance'))['current_balance__sum'] or 0
    wallet_count = wallets.count()

    total_income = Income.objects.filter(wallet__in=wallets).aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Expense.objects.filter(wallet__in=wallets).aggregate(Sum('amount'))['amount__sum'] or 0

    pending_operations = Operation.objects.filter(wallet__in=wallets, status='pending').count()
    archived_documents = Document.objects.filter(wallet__in=wallets, archived=True).count()

    # Liste des mouvements (opérations)
    operations_incomes = [
        {
            'wallet': income.wallet.name,
            'amount': float(income.amount),
            'status': 'Validé',  # adapte selon ton modèle
            'type': 'income',
            'date': income.date.isoformat(),
        }
        for income in Income.objects.filter(wallet__in=wallets)
    ]

    operations_expenses = [
        {
            'wallet': expense.wallet.name,
            'amount': float(expense.amount),
            'status': 'En attente',  # adapte selon ton modèle
            'type': 'expense',
            'date': expense.date.isoformat(),
        }
        for expense in Expense.objects.filter(wallet__in=wallets)
    ]

    all_movements = operations_incomes + operations_expenses
    # Trie par date décroissante
    all_movements.sort(key=lambda x: x['date'], reverse=True)

    data = {
        'username': user.username,
        'role': user.role,
        'total_treasury': total_treasury,
        'wallet_count': wallet_count,
        'total_income': total_income,
        'total_expense': total_expense,
        'pending_operations': pending_operations,
        'archived_documents': archived_documents,
        'movements': all_movements,
    }

    return Response(data)
