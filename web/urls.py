
from django.urls import path
from web import views


app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>/', views.category, name='category'),
    path('product/<int:id>/', views.product, name='product'),
    path('buynow/<int:id>/', views.buynow, name='buynow'),


   
]
