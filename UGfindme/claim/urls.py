from django.urls import path
from .import views
app_name = 'claim'


urlpatterns =[
    path('', views.claim_detail, name='claim_detail'),
    path('add/<int:product_id>/', views.claim_add,name='claim_add'),
    path('remove/<int:product_id>/', views.claim_remove,name='claim_remove'),
]