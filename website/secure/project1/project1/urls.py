from django.contrib import admin
from django.urls import path, include  # ✅ include is needed

urlpatterns = [
    path('', include('myapp.urls')),   # ✅ This connects your app
    path('admin/', admin.site.urls),
]