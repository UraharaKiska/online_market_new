from django.db import models
from users.models import CustomUser
from product.models import Product
from django.db.models import Q, F
# Create your models here.
from django.urls import reverse






class Order_status(models.Model):
    status = models.CharField(verbose_name="status", max_length=100)
    
    
    def __str__(self):
        return self.status

         
    
class Orders(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    second_name = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(CustomUser, verbose_name="user", on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    personal_order_id = models.IntegerField(verbose_name="personal order",blank=True, null=False) # redefine savee
    full_order_id = models.CharField(verbose_name="full order_id", blank=True, unique=True, null=False)
    status = models.ForeignKey(Order_status, verbose_name="status", on_delete=models.CASCADE, default=3)
    date_create = models.DateTimeField(auto_now_add=True) 
    date_update = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(default=0, blank=True, max_digits=10, decimal_places=0)
    paid = models.BooleanField(default=False)
    
    
    def get_absolute_url(self):
        return reverse('my_order', kwargs={'order_slug': self.full_order_id})
    
    
    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        
        query = Orders.objects.filter(user=self.user).last()
        if query: 
            order = query.personal_order_id + 1
        else: 
            order = 1
        self.personal_order_id = order
        self.full_order_id = f"{self.user.id}-{self.personal_order_id}"
        super().save(*args, **kwargs)
  
    def __str__(self):
        return self.full_order_id

    class Meta:
        constraints = [
            models.CheckConstraint(
                check = Q(personal_order_id__gte=0),
                name = 'check_personal_order_id',
            )
        ]
           

    
    
class Orders_Item(models.Model):
    product = models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="count")
    full_order = models.ForeignKey(Orders, to_field='full_order_id', verbose_name="order id", on_delete=models.CASCADE)
    price_for_one = models.IntegerField(default=0, blank=True)
    
    def __str__(self):
        return self.full_order.full_order_id

    def save(self, *args, **kwargs):
        product = Product.objects.get(id=self.product.id)
        new_price = product.new_price
        old_price = product.old_price
        self.price_for_one = new_price if new_price else old_price
        order = Orders.objects.filter(full_order_id=self.full_order).update(total_price = F('total_price') + self.count * self.price_for_one)
        # order.save()
        super().save(*args, **kwargs)
        
        
    class Meta:
        constraints = [
            models.CheckConstraint(
                check = Q(count__gte=0),
                name = 'check_product_count',
            )
        ]
    
  