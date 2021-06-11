from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    #If path is empty then flow will go to ProductViewHome class in views.py
    path('',views.ProductViewHome.as_view(),name='home'),
    #path('',views.home,name='home'),
    

    #If path is wrogn then flow will go to ProductViewWrogn class in views.py
    path('wrogn',views.ProductViewWrogn.as_view(),name='wrogn'),
    #path('wrogn',views.wrogn,name='wrogn'),
    

    #If path is flying then flow will go to ProductViewFlying class in views.py
    path('flying',views.ProductViewFlying.as_view(),name='flying'),
    #path('flying',views.flying,name='flying'),
    

    #If path is peter then flow will go to ProductViewPeter class in views.py
    path('peter',views.ProductViewPeter.as_view(),name='peter'),
    #path('peter',views.peter,name='peter'),

    path('cart',views.ProductViewCart.as_view(),name='cart'),

   # path('showcart',views.ProductViewShowCart.as_view(),name='cart'),


    path('product/<int:pk>',views.ProductViewProduct.as_view(),name='product'),


] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)