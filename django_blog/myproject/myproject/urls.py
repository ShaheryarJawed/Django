from django.contrib import admin
from django.urls import path
from blog.views import register, login_view, home  # Ensure 'blog' is the name of your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # URL for the home page
    path('register/', register, name='register'),  # URL for the registration page
    path('login/', login_view, name='login'),  # URL for the login page
]
