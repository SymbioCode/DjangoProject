from django.shortcuts import render
from django.views.generic import TemplateView
from pizzashop.models import *


class PizzaView(TemplateView):
    template_name = "pizza_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['pizzas_list'] = Pizza.objects.all()
        return context
