from django.db import models
from users.models import CustomUser
from product.models import Product
from django.db.models import Q
# Create your models here.






class Order_status_types(models.Model):
    status = models.CharField(verbose_name="status", max_length=100)
    
    
    def __str__(self):
        return self.status

         
    
class Orders_data(models.Model):
 
    user = models.ForeignKey(CustomUser, verbose_name="user", on_delete=models.CASCADE, null=False)
    personal_order_id = models.IntegerField(verbose_name="personal order",blank=True, null=False) # redefine savee
    full_order_id = models.CharField(verbose_name="full order_id", blank=True, unique=True, null=False)
    status = models.ForeignKey(Order_status_types, verbose_name="status", on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True) 
    date_update = models.DateTimeField(auto_now=True)
    
    
    
    
    def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        
        query = Orders_data.objects.filter(user=self.user).last()
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
           
    
class Orders_inform(models.Model):
    product = models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name="count")
    full_order = models.ForeignKey(Orders_data, to_field='full_order_id', verbose_name="order id", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.full_order.full_order_id


    class Meta:
        constraints = [
            models.CheckConstraint(
                check = Q(count__gte=0),
                name = 'check_product_count',
            )
        ]
     