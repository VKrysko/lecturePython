from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django.urls import reverse

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=200)
    url= models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products', blank=True)
    
    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['url','id', 'name']),
            models.Index(fields=['name'], name='name_idx'),
                  ]
    
    def __str__(self):
        return f"{self.name} " 

    def get_absolute_url(self):
        return reverse('index',
                        args=[ self.url])
       
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    starting_bid  = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(auto_now=True)
    seller=models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['url','id', 'name']),
            models.Index(fields=['name'], name='name_products_idx'),
                  ]

    def __str__(self):
        return f"{self.name} {self.starting_bid}$ {self.seller}"    
  
    def get_absolute_url(self):
        return reverse('detail',
                        args=[self.id, self.url])

class Watchlist(models.Model):
    user_watchlist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_watchlist')
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_item')
    
    def __str__(self):
        return f"{self.user_watchlist} {self.product_item}"

class Bid(models.Model):
    user_bid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bid')
    item_bid = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item_bid')
    bid = models.IntegerField()
    date_bid = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user_bid} {self.item_bid.name} {self.bid}"    


class Comment(models.Model):
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment', null=True, blank=True)
    product_comment = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comment', null=True, blank=True)
    comment = models.CharField(max_length=1024)
    date_comment = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user_comment} {self.product_comment.name} {self.comment}"     

