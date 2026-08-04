from django.db import models
from django.conf import settings
from wallet.models import Wallet  # Assure-toi que ce modèle existe

class Operation(models.Model):

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        related_name="operations",
    )

    title = models.CharField(
        max_length=255,
    )

    subtitle = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    motif = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    dateTime = models.DateTimeField()

    amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    positive = models.BooleanField(
        default=True,
    )

    badge = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    color = models.CharField(
        max_length=20,
        default="#0066FF",
    )

    icon = models.CharField(
        max_length=50,
        default="account_balance_wallet",
    )

    currency = models.CharField(
        max_length=3,
        choices=(
            ("usd", "USD"),
            ("cdf", "CDF"),
            ("eur", "EUR"),
        ),
        default="usd",
    )

    category = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    attachmentsAllowed = models.BooleanField(
        default=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='operations_created',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-dateTime"]

    def __str__(self):
        return f"{self.wallet.name} - {self.title}"
