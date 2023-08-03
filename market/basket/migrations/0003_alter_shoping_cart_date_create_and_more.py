
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_alter_shoping_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoping_cart',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='shoping_cart',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
