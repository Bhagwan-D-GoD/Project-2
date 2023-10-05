from django.urls import path
from . import views

urlpatterns = [
    path('stockdata/', views.stock_data, name='stock_data'),
    path('formdata/',views.addstockform_view,name='formdata'),
    path('portfolio/',views.portfolio,name="portfolio"),
]
