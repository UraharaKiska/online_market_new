from decimal import Decimal
from django.conf import settings
from product.models import Product


class Cart:

    def __init__(self, request):


        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            print('HUI')
            # save empty cart in the sessions
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        price = product.old_price
        sell = product.new_price
        if product.new_price:
            price = sell

        if product_id not in self.cart:
            print('HUUUUI')
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        if self.cart[product_id]['quantity'] <= 0:
            self.remove(product)
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for key, item in cart.items():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

