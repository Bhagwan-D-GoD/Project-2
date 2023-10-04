from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf





def stock_data(request):
    ticker = 'AAPL'  # Replace with the stock symbol you want to fetch
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")  # Fetch 1-year historical data

    context = {'data': data}
    return render(request, 'stock_data.html', context)








########################for form#################
from .form import addstockform
def addstockform_view(request):
    form=addstockform();
    if request.method=='POST':
        form=addstockform(request.POST)
        if form.is_valid():
            form.save()
    context={"form":form}
    return render (request,"allstock.html",context)        
    
    
    
    


###########################for portfolio #############
from .models import stockportfolio
def portfolio(request):
    if request.session.has_key('session_username'):
        data=stockportfolio.objects.filter(user_id=2)
        return render(request,'portfolio.html',{'data':data})