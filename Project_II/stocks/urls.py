from django.urls import path
from .import views

urlpatterns = [
    path('stockdata/', views.stock_data, name='stock_data'),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('delete_portfolio/<int:pk>/', views.delete_portfolio, name='delete_portfolio'),
]
