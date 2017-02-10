from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from .models import *

# Create your views here.

def home_page(request):
    return render(request, 'amoreserumores_app/home_page.html', {})

class ProductList(ListView):

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProductDetail(ListView):

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now']   
