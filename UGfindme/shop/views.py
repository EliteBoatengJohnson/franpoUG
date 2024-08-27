from django.shortcuts import render,get_object_or_404,redirect
from .models import Category, Product, User
from claim.forms import ClaimAddProductForm
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
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
        if request.user.is_authenticated:
            return redirect('shop:product_list')
        
        form = LoginForm()
        return render(request,'shop/users/login.html', {'form':form})

    elif request.method =='POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                messages.success(request,f"Hi {username.title()}, welcome back! ")
                return redirect('shop:product_list')
            messages.error(request,f"invalid username or password")
    return render(request,'shop/users/login.html', {'form':form})


#log-Out
def Sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('shop:login')