from rest_framework.viewsets import ModelViewSet

from order.models import Order,Order_detail
from order.serializers import OrderSerializer,OrderDetailSerializer


class OrderViewset(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



class OrderDetailViewset(ModelViewSet):
    queryset = Order_detail.objects.all()
    serializer_class = OrderDetailSerializer
