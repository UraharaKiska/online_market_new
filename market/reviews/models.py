from django.db import models
from product.models import Product
from users.models import CustomUser
from django.db.models import CheckConstraint, Q, UniqueConstraint




class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_create = models.DateField(auto_now_add=True)
    
    
    class Meta:
        constraints = [
            CheckConstraint(
                check = Q(rating__gt=0) and Q(rating__lte=5),
                name = 'chek_rating_value',
            ),
            UniqueConstraint(
                fields=["user", "product"], 
                name="Distinct_user_review"
            ),
            
        ]
           