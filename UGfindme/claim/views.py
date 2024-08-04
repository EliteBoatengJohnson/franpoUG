from django.shortcuts import render,get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .claim import Claim
from .forms import ClaimAddProductForm

@require_POST
def claim_add(request,product_id):
    claim = Claim(request)
    product = get_object_or_404(Product,id=product_id)
    form = ClaimAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        claim.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    return redirect('claim:claim_detail')


@require_POST
def claim_remove(request,product_id):
    claim =Claim(request)
    product = get_object_or_404(Product,id=product_id)
    claim.remove(product)
    return redirect('claim:claim_detail')

def claim_detail(request):
    claim = Claim(request)
    return render(request, 'claim/detail.html',{'claim': claim})