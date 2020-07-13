from rest_framework.routers import DefaultRouter
from shop.views import ShopViewSet
from users.views import UserViewSet, LoginView, RegisterView

router = DefaultRouter()
router.register('shops', ShopViewSet, basename='shop-list')
router.register('users', UserViewSet, basename='users-list')
router.register('login', LoginView, basename='login')
router.register('register', RegisterView, basename='logout')
