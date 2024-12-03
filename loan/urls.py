from rest_framework.routers import DefaultRouter
from .views import LoanViewSet

router = DefaultRouter()
router.register(r'loan', LoanViewSet)

urlpatterns = router.urls 
