from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.chart_view, name='chart'),
    path('graph/', views.main_view, name='graph'),
]