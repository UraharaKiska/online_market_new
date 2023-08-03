from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    product_type = models.ForeignKey('Product_type', on_delete=models.PROTECT)
    old_price = models.IntegerField(null=False)
    new_price = models.IntegerField(null=True, blank=True)
    count = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})
    
    
    class Meta:
        verbose_name = "Products list"
        ordering = ['date_create']
        
        
        
class Product_type(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Product type')
    slug = models.SlugField(max_length=120, unique=True, db_index=True, verbose_name='URL')
    
    def get_absolute_url(self):
        return reverse('type', kwargs={'product_type_slug': self.slug})

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = "Product type"
        ordering = ['id']
        
        
class ProductPhoto(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photo_product/%Y/%m/%d", null=True, verbose_name='photo')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
            return self.id_product.name


class Product_rating(models.Model):
    product = models.OneToOneField(Product, related_name='rating', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    