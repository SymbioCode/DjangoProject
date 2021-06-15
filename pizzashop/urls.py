import math
from django.urls import path, include
from pizzashop.views import *

urlpatterns = [
    path('pizzas_list/', PizzaView.as_view())

]
