# online_market

---------------------------------------
sql query for card-photo element:
"""
    select name, old_price, count, ph.photo  from product_product pr
    inner join ( 
        select distinct on (id_product_id) * from product_productphoto) as ph on pr.id = ph.id_product_id  
"""

with django orm:
"""
    ProductPhoto.objects.select_related('id_product').distinct('id_product')
"""
-----------------------------------------



