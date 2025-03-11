from django.shortcuts import render, redirect
from . forms import ProductForm
from .models import Product
# Create your views here.

# HOME VIEW
def home(request):
    return render(request, 'invApp/home.html')

# CREATE VIEW
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Replace with your success URL
    else:
        form = ProductForm()
    
    return render(request, 'invApp/product_form.html', {'form': form})
    
# Read VIEW
def product_list_view(request):
    products  = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})

#   UPDATE VIEW
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id) # get is a special method that returns a single object  based on product_id or primary key
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})    
    
            
        
#  DELETE VIEW
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return render('product_list')
    return render(request, 'invApp/product_delete.html', {'product': product})


