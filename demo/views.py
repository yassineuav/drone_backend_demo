from rest_framework import viewsets

from .models import Drone, DroneTest, Order, OrderHistory, OrderStatus, Coordinates
from .serializers import DroneTestSerializer, DroneSerializer, HistoryStatusSerializer, StatusSerializer, OrderSerializer, CoordinatesSerializer


class DroneViewSet(viewsets.ModelViewSet):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()


class DroneTestViewSet(viewsets.ModelViewSet):
    serializer_class = DroneTestSerializer
    queryset = DroneTest.objects.all()


class CoordinatesViewSet(viewsets.ModelViewSet):
    serializer_class = CoordinatesSerializer
    queryset = Coordinates.objects.all()


class OrderStatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = OrderStatus.objects.all()


class OrderHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistoryStatusSerializer
    queryset = OrderHistory.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    # queryset = Order.objects.all()
    # queryset = Order.objects.prefetch_related('status_history_set').all()
    # queryset = Order.objects.select_related('orderhistory_set').all()
    queryset = Order.objects.prefetch_related('order_history').all()
    serializer_class = OrderSerializer


