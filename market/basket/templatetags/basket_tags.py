from django import template
from product.models import ProductPhoto

register = template.Library()


@register.simple_tag(name="getphoto")
def get_first_photo(id):
        photo = ProductPhoto.objects.filter(id_product=id)
        
        return {'photo': photo}