from django.urls import path
from . import views 

urlpatterns = [
    path('', views.showAllProduct, name='showProducts'),
    path('product/<str:pk>/', views.productDetails, name='productDetails'),

    path('addProduct/', views.addProducts, name='addProduct'),
    path('updProduct/<int:pk>/', views.updateProducts, name='uptProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='delProduct'),

    path('search/', views.searchBar, name='search'),
]  
