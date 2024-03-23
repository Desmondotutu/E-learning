from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.register, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]