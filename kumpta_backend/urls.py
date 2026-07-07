from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

def home(request):
    return JsonResponse(
        {"message": "Kumpta backend actif 🚀"},
        json_dumps_params={'ensure_ascii': False}
    )

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('api/accounts/', include('accounts.urls')),

    # 🔐 JWT LOGIN
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]