from django.contrib import admin
from .models import Category, Product, Watchlist, Bid, Comment, User

# Register your models here.
admin.site.register(User)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    prepopulated_fields = {'url': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'starting_bid', 'available', 'created', 'seller']
    list_filter = ['available', 'created']
    list_editable = ['starting_bid', 'available']
    prepopulated_fields = {'url': ('name',)}
admin.site.register(Product, ProductAdmin)

admin.site.register(Watchlist)
admin.site.register(Bid)
admin.site.register(Comment)
