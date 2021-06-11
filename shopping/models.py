from django.db import models
from users.models import Customer
# Create your models here.

#This is a company table in which all the details of the companies are stored.
class Company(models.Model):
    comp_id =models.TextField()

#This is a user table in which all the details of the users are stored.
class User(models.Model):
    user_id =models.TextField()

#This is a product table in which all the details of the product are stored.
class Product(models.Model):
    comp_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    prod_id= models.TextField()
    prod_img= models.ImageField(upload_to='productimg')
    prod_name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField( default='UW' , max_length=15)
    available= models.TextField()
    
#This is a cart table in which all the details of the user's cart are stored.
#class Cart(models.Model):
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    #cart_id = models.TextField()
    #prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    #quantity= models.PositiveIntegerField(default=1)

#This is a order placed table in which all the details of the orders of user are stored.
class OrderPlaced(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)   
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    Customer = models.TextField()   
    prod_id = models.TextField()
    quantity= models.PositiveIntegerField(default=1)
   