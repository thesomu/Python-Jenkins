from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.customer, name='customer'),
    path('register', views.register, name='register'),
    path('custadmin',views.custadmin,name='custadmin'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('admindelete/<int:id>',views.admindelete,name='admindelete'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('shipping', views.shipping, name='shipping'),
    path('profile', views.Profile, name='profile'),
    path('custdelete/<int:id>', views.custdestroy, name='delete'),
    path('custedit/<int:id>', views.custedit, name='edit'),
    path('custupdate/<int:id>', views.custupdate, name='update')
]
