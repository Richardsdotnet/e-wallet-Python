from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('wallet', views.WalletViewSet)
router.register('transaction', views.TransactionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
