from django.contrib import admin

# Register your models here.


#company model is registered here.
from .models import Company
admin.site.register(Company)

#user model is registered here.
from .models import User
admin.site.register(User)

#product model is registered here.
from .models import Product
admin.site.register(Product)

#cart model is registered here.
from .models import Cart
admin.site.register(Cart)

#orderplaced model is registered here.
from .models import OrderPlaced
admin.site.register(OrderPlaced)

