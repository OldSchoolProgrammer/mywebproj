from django.shortcuts import render
from django.views.generic import ListView
from . import models


class CustomerListView(ListView):
    model = models.Customers
    context_object_name = 'customers'
