from django.db import models
from product.models import Product
from users.models import CustomUser
from django.db.models import CheckConstraint, Q, UniqueConstraint, F
from product.models import Product_rating



class Reviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
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
           
    
    def save(self, *args, **kwargs):
        product_rating = Product_rating.objects.filter(product=self.product).first()
        if product_rating is None:
            product_rating = Product_rating.objects.create(product=self.product)
        count_review = len(Reviews.objects.filter(product=self.product)) + 1
        product_rating.rating = (float(product_rating.rating) + float(self.rating)) / float(count_review)
        print(product_rating.rating)
        product_rating.save(update_fields=["rating"])
        super().save(*args, **kwargs)

    