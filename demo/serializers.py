from rest_framework import serializers

from .models import Drone, DroneTest, Order, OrderStatus, Coordinates, OrderHistory


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = "__all__"


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = "__all__"


class DroneTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = DroneTest
        # fields = ['id', 'status', 'name', 'battery']
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = "__all__"


class HistoryStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = '__all__'
        # depth = 1


class OrderSerializer(serializers.ModelSerializer):
    # status_history = HistoryStatusSerializer(many=True, read_only=True)
    status_history = serializers.SerializerMethodField()

    def get_status_history(self, obj):
        order_histories = OrderHistory.objects.filter(order_history_id=obj)
        return HistoryStatusSerializer(order_histories, many=True).data

    # status, _created = OrderHistory.objects.get_or_create(order_history_id=instance.id)
    # print(f'creating new status {status}  | else _created {_created}')

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        OrderHistory.objects.create(order_history_id=order.id)
        print(f'creating new order history status')
        return order

    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['id', 'weight', 'description', 'trigger', 'updated_at', 'status', 'status_id', 'status_history']
        depth = 1



