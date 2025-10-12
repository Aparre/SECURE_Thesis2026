from django.contrib import admin
from .models import Category, Product, Customer, Order

# yt https://youtu.be/Cp7geK7xjyI?si=QzFbcWSJWG9REKrK
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
