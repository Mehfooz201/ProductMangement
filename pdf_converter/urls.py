from django.urls import path
from . import views 

urlpatterns = [
    path('showproducts/', views.showProducts, name='showproducts'),
    path('pdfreport/', views.pdfReportCreated, name='pdf_report'),
]  
