from rest_framework.routers import DefaultRouter

from account.api_views import LoginView
from order.api_views import OrderViewset, OrderDetailViewset
from product.api_views import ProductViewset,CategoryViewset


router = DefaultRouter()
##Products
router.register('product',ProductViewset,basename='product')
router.register('category',CategoryViewset,basename='category')

#Orders
router.register('order',OrderViewset,basename='order')
router.register('order_detail',OrderDetailViewset,basename='order_detail')


##AUTH
router.register('login',LoginView,basename='login')
