from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_data(request):

    user = request.user


    data = {

        "username": user.username,

        "role": user.role,

        "treasury": 1200000,

        "active_wallets": 24,

        "pending_operations": 7,

        "archived_documents": 18,

    }


    return Response(data)