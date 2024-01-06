from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('customers/', views.customer, name='all_customers'),
    path('add_new/', views.add_new, name='add_customer'),
    path('edit/<int:id>',views.edit,name='Customer_Modify'),
    path('delete/<int:id>',views.delete,name='Customer_Delete'),
]