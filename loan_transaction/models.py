from django.db import models

from django.db import models
from django.utils.translation import gettext_lazy as _

class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DISBURSEMENT = 'Disbursement', _('Disbursement')
        REPAYMENT = 'Repayment', _('Repayment')
        OTHER = 'Other', _('Other')

TRANSACTION_STATUS = (
    ("PENDING","PENDING"),
    ("VERIFIED","VERIFIED"),
    ("REJECTED","REJECTED"),
)




class TransactionStatus(models.TextChoices):
    transaction_id = models.CharField(max_length=20, unique=True, editable=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30, choices=TRANSACTION_STATUS, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {self.status}"

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            import uuid
            self.transaction_id = str(uuid.uuid4())[:20]  
        super().save(*args, **kwargs)

