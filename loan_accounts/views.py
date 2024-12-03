from django.shortcuts import render

from rest_framework import viewsets
from .models import Loan_accounts
from .serializers import Loan_accountsSerializer

class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Loan_accounts.objects.all()
    serializer_class = Loan_accountsSerializer
    queryset = Loan_accounts.objects.all()
    serializer_class = Loan_accountsSerializer
    filterset_fields = ['currency', 'user']
    ordering_fields = ['created']
    ordering = ['created']


