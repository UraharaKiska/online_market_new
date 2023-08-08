from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import CheckConstraint, Q

from users.models import *
from product.models import *


class Shoping_cart(models.Model):
    id_user = models.ForeignKey(CustomUser, verbose_name="user", on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name="count", default=1)
    # in_stock = models.BooleanField(default="True", null=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            CheckConstraint(
                check = Q(quantity__gte=0),
                name = 'check_quantity_cart_product',
            )
        ]
           
  
        
    def clean(self):
        if self.quantity < 0:
            raise ValidationError({'quantity': _('Quantity cant be less than "0"! ')})
    
    

