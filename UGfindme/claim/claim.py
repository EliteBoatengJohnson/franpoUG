from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Claim:
    def __init__(self, request):
        """This initialize the Claim"""
        self.session = request.session
        claim = self.session.get(settings.CLAIM_SESSION_ID)
        if not claim:
            # save an empty claim request in the session 
            claim = self.session[settings.CLAIM_SESSION_ID]={}
        self.claim = claim

    def add(self, product, quantity=1, override_quantity=False):
        """This Method adds a Item or product to the cart or update its quantity"""
        product_id = str(product.id)
        if product_id not in self.claim:
            self.claim[product_id] = {
                'quantity': 0
            }
        if override_quantity:
            self.claim[product_id]['quantity'] = quantity
        else:
            self.claim[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """Remove a product from the claim box"""
        product_id = str(product.id)
        if product_id in self.claim:
            del self.claim[product_id]
            self.save()

    def __iter__(self):
        """Iterate over the items in the cart and get the products from the database"""
        product_ids = self.claim.keys()
        # get the products/items object and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        claim = self.claim.copy()
        for product in products:
            claim[str(product.id)]['product'] = product
        for item in claim.values():
            yield item
    
    def __len__(self):
        """Count all items in the claim"""
        return sum(item['quantity'] for item in self.claim.values())
    
    def clear(self):
        # remove claims from session
        del self.session[settings.CLAIM_SESSION_ID]
        self.save()