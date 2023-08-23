from django.urls import path, include
from rest_framework import routers

import user.views
from . import views

router = routers.DefaultRouter()
router.register('wallet', views.WalletViewSet)
router.register('transaction', views.TransactionViewSet)
router.register('user', user.views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
