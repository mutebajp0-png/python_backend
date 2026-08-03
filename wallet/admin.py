from django.contrib import admin

from .models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "currency",
        "current_balance",
        "get_administrator",
        "is_active",
        "created_at",
    )


    search_fields = (
        "name",
    )


    list_filter = (
        "currency",
        "is_active",
    )


    def get_administrator(self, obj):
        return obj.administrator.username

    get_administrator.short_description = "Administrateur"