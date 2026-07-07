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

        "treasury": 0,

        "active_wallets": 0,

        "pending_operations": 0,

        "archived_documents": 0,

    }


    return Response(data)