from rest_framework import serializers
from .models import Loan_accounts

class Loan_accountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_accounts
        fields = [
            'account_id',
            'user',
            'account_number',
            'currency',
            'interest_rate',
            'created',
            'last_withdrawal_date',
            'withdrawal_limit',
            'maturity_date'
        ]
