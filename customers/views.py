from django.shortcuts import render
from django.views.generic import ListView
from .models import Customers


class CustomerListView(ListView):
    model = Customers
    context_object_name = 'customers'
