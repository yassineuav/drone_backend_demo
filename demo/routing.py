from django.urls import re_path

from . import consumers


websocket_urlpatterns = [
    re_path(r"^ws/order/$", consumers.OrderConsumer.as_asgi()),
    re_path(r"^ws/drone/$", consumers.DroneConsumer.as_asgi()),
    re_path(r"^ws/test/$", consumers.DroneTestConsumer.as_asgi()),
]
