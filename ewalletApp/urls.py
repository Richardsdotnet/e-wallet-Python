from rest_framework import routers

from ewalletApp import views

router = routers.DefaultRouter()
router.register('walletApp', views.WalletViewSet)