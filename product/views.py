from django.shortcuts import render
from .models import Product, ProductImage, ProductVariant, ProductVariantPrice, Variant  

def home(request):

    return render(request, 'main/search.html')
