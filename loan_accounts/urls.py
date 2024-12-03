from rest_framework.routers import DefaultRouter
from .views import AccountsViewSet

router = DefaultRouter()
router.register(r'Loan_accounts', AccountsViewSet)

urlpatterns = router.urls
