from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Borrower, Loan
from .serializers import BorrowerSerializer, LoanSerializer

class BorrowerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Borrowers to be viewed or edited.
    """
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict to only the logged-in user's borrower record
        return super().get_queryset().filter(user=self.request.user)

class LoanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Loans to be viewed or edited.
    """
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Restrict loans to those associated with the logged-in user
        user = self.request.user
        return super().get_queryset().filter(borrower__user=user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the borrower
        borrower = Borrower.objects.get(user=self.request.user)
        serializer.save(borrower=borrower)

