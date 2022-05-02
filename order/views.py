from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from order.models import SalesOrder
from order.serializers import OrderSerializer


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


# Create your views here.
class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer
