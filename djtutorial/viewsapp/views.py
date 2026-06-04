from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Products
from .forms import ProductForm

# Create your views here.

def home_view(request):
    products = Products.objects.all()
    
    return render(request, 'viewsapp/home_view.html', {
        'products': products
    })
    
def product_details(request, id):
    product = get_object_or_404(Products, id=id)
    
    return render(request, 'viewsapp/product_details.html', {'product': product})

def add_product(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_view')
        
    return render(request, 'viewsapp/form_ui.html', {'form': form})

class ProductListView(ListView):
    model = Products
    template_name = 'viewsapp/home_view.html'
    context_object_name = 'products'
    
class ProductDetails(DetailView):
    model = Products 
    template_name = 'viewsapp/product_details.html'
    context_object_name='product'
    
class ProductUpdateView(UpdateView):
    model = Products
    fields = ['product_name', 'product_quantity', 'category']
    template_name = "viewsapp/form_ui.html"
    success_url = reverse_lazy('home_view')
    
    
class ProductDeleteView(DeleteView):
    model = Products
    template_name = "viewsapp/delete_product.html"
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'
    
def product_api(request):
    products = Products.objects.all()
    
    data = []
    
    for product in products:
        data.append({
            'Product name': product.product_name,
            'Category': product.category.product_category
        })
        
    return JsonResponse(data, safe=False)