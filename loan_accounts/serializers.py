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

from rest_framework import serializers
from .models import Loan_withdrawal, Loan_transfer

class LoanWithdrawalSerializer(serializers.ModelSerializer):
    """Serializer for Loan Withdrawal model."""

    class Meta:
        model = Loan_withdrawal
        fields = '__all__'


class CreateLoanWithdrawalSerializer(serializers.ModelSerializer):
    """Serializer for creating a Loan Withdrawal."""

    class Meta:
        model = Loan_withdrawal
        fields = ['account_number', 'amount']


class LoanTransferSerializer(serializers.ModelSerializer):
    """Serializer for Loan Transfer model."""

    class Meta:
        model = Loan_transfer
        fields = '__all__'


class CreateLoanTransferSerializer(serializers.ModelSerializer):
    """Serializer for creating a Loan Transfer."""

    class Meta:
        model = Loan_transfer
        fields = ['destination_account_number', 'amount']

