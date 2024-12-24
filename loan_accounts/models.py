import uuid
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from .choices import CURRENCY_CHOICES

class Loan_accounts(models.Model):
    account_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.PositiveBigIntegerField(null=True, blank=True, unique=True)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES)
    interest_rate = models.DecimalField(decimal_places=2, max_digits=3, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    last_withdrawal_date = models.DateTimeField(blank=True, null=True)
    withdrawal_limit = models.DecimalField(decimal_places=2, max_digits=10, default=1000000)
    maturity_date = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.last_withdrawal_date

    class Meta:
        verbose_name = "Loan_account"
        verbose_name_plural = "Loan_accounts"



TRANSACTION_STATUS_CHOICES = (
    ("SUCCESSFUL", "SUCCESSFUL"),
    ("FAILED", "FAILED"),
    ("PENDING", "PENDING"),
)

class Transaction(models.Model):    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="%(class)s_transactions"  # This dynamically sets the related_name
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    statuss = models.CharField(max_length=15, choices=TRANSACTION_STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-timestamp']

class Loan_withdrawal(Transaction):
    account_number = models.CharField(max_length=11)
    transaction_type = models.CharField(max_length=8, default='WITHDRAWAL')

    def __str__(self):
        return f"Loan Withdrawal {self.id} - {self.amount}"

class Loan_transfer(Transaction):
    destination_account_number = models.CharField(max_length=11)
    transaction_type = models.CharField(max_length=8, default='TRANSFER')

    def __str__(self):
        return f"Loan Transfer {self.id} - {self.amount}"




