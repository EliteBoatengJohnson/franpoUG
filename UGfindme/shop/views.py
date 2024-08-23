from django.shortcuts import render,get_object_or_404
from .models import Category, Product
from claim.forms import ClaimAddProductForm
from .forms import LoginForm
from django.contrib.auth import login, authenticate
# Create your views here.
def product_list(request,category_slug=None):
    category = None
    categories =Category.objects.all()
    products =Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products =products.filter(category=category)
    return render(
        request,
        'shop/product/list.html',
        {
            'category': category,
            'categories': categories,
            'products':products
        }
    )


def product_detail(request,id,slug):
    product =get_object_or_404(
        Product, id=id, slug=slug, available=True
    )
    claim_product_form = ClaimAddProductForm()
    return render(
        request,
        'shop/product/detail.html',
        {'product':product,'claim_product_form': claim_product_form}
    )

#  login form for the project
def Sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'users/login.html', {'form':form})
