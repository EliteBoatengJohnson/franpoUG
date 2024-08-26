from django.urls import path
from . import views

app_name = 'shop'

urlpatterns =[
    path('login/', views.Sign_in, name='login'),
    path('logout/', views.Sign_out, name='logout'),
    path('', views.product_list,name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
    
]