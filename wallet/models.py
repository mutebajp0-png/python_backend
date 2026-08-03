from django.conf import settings
from django.db import models


class Wallet(models.Model):

    CURRENCIES = (
        ("USD", "Dollar américain"),
        ("CDF", "Franc congolais"),
        ("EUR", "Euro"),
    )

    name = models.CharField(
        max_length=150,
        verbose_name="Nom du département",
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    currency = models.CharField(
        max_length=3,
        choices=CURRENCIES,
        default="USD",
    )

    initial_balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
    )

    current_balance = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        default=0,
    )

    color = models.CharField(
        max_length=20,
        default="#0066FF",
    )

    icon = models.CharField(
        max_length=50,
        default="account_balance_wallet",
    )

    # Administrateur propriétaire du département
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="owned_departments",
        verbose_name="Administrateur",
    )

    # Manager responsable du département
    manager = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="managed_department",
        verbose_name="Manager du département",
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Département"
        verbose_name_plural = "Départements"

    def __str__(self):
        return self.name