from django.db import models
from django.conf import settings

from wallet.models import Wallet


class Income(models.Model):

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        related_name="incomes",
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    amount = models.DecimalField(
        max_digits=18,
        decimal_places=2,
    )

    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.wallet.name} - {self.title}"