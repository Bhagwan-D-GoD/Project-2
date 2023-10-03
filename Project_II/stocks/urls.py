from django.urls import path
from . import views

urlpatterns = [
    path('stockdata/', views.stock_data, name='stock_data'),
    path('portfolio/',views.porfolio,name='portfolio'),
]
