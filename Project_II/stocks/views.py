from django.shortcuts import render,redirect
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf
from django.contrib.auth.models import User
from .models import stockportfolio
from .form import addstockform



def stock_data(request):
    ticker = 'AAPL'  # Replace with the stock symbol you want to fetch
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")  # Fetch 1-year historical data

    context = {'data': data}
    return render(request, 'stock_data.html', context)








########################for form#################
def addstockform_view(request):
    uname=request.session.get('username')
    if request.session.has_key('username'):
        uname=request.session.get('username')
        form=addstockform();
        if request.method=='POST':
            form=addstockform(request.POST)
        if form.is_valid():
            portfoliostock=stockportfolio()
            portfoliostock.user=User.objects.get(username=uname)
            realuser=portfoliostock.user
            stocksymbol = form.cleaned_data['stocksymbol']   
            quantity = form.cleaned_data['quantity']   
            buy_price = form.cleaned_data['buy_price']  
            try:
                item = stockportfolio.objects.filter(user=realuser).get(stocksymbol=stocksymbol)
                item.quantity += quantity
                item.save()
            except stockportfolio.DoesNotExist:
                portfoliostock = stockportfolio(
                    stocksymbol=stocksymbol,
                    quantity=quantity,
                    buy_price=buy_price,
                    user=User.objects.get(username=uname)
                )
                portfoliostock.save()
            return redirect("portfolio")
        content={
            'form':form,
        }    
        return render(request,'allstock.html',content)
    
    
    
    


###########################for portfolio #############
def portfolio(request):
    uname=request.session.get('username')
    # for adding the stocks
    if request.method=='POST':
            form=addstockform(request.POST)
            if form.is_valid():
                portfoliostock=stockportfolio()
                portfoliostock.user=User.objects.get(username=uname)
                realuser=portfoliostock.user
                stocksymbol = form.cleaned_data['stocksymbol']   
                quantity = form.cleaned_data['quantity']   
                buy_price = form.cleaned_data['buy_price']  
                try:
                    item = stockportfolio.objects.filter(user=realuser).get(stocksymbol=stocksymbol)
                    item.buy_price = (item.buy_price * item.quantity + buy_price * quantity )/ (item.quantity + quantity)
                    item.quantity += quantity
                    item.save()
                except stockportfolio.DoesNotExist:
                    portfoliostock = stockportfolio(
                        stocksymbol=stocksymbol,
                        quantity=quantity,
                        buy_price=buy_price,
                        user=User.objects.get(username=uname)
                    )
                    portfoliostock.save()
                return redirect("portfolio")
    form=addstockform()
    user_instance=User.objects.get(username=uname)#to get user instance
    portfoliostock=stockportfolio()
    # portfoliostock.user=User.objects.get(username=uname)
    # realuser=portfoliostock.user
    item= stockportfolio.objects.filter(user=user_instance)
    # if the user doesnot have any data in the portfolio
    buysum=0
    currentsum=0
    check= stockportfolio.objects.filter(user=user_instance).count()
    if check != 0:
        print("pass")
    # to update the current price in database
        for symbol in item:
            stock_symbol=symbol.stocksymbol
            stock=yf.Ticker(stock_symbol)
            price = stock.history(period="1d")["Close"].iloc[0]
        #symbol.current_price=price
            stockportfolio.objects.filter(user=user_instance,stocksymbol=stock_symbol).update(current_price=price)
    # to identify profit or loss   
        for symbol in item:
            buysum=0
            buyindividual=symbol.buy_price*symbol.quantity
            buysum+=buyindividual
            currentsum=0
            currentindividual=symbol.current_price*symbol.quantity
            currentsum+=currentindividual
        data=stockportfolio.objects.filter(user_id=user_instance)
        amount = 0
        if buysum>currentsum:
            amount=buysum-currentsum
            message='Total loss'
        elif buysum<=currentsum:
            amount=currentsum-buysum
            message='Total Profit'
        return render(request,'portfolio.html',{'data':data,'amount':amount,'message':message,'form':form,})
    else:
        message="NO Data To Show. Please Add Your Stocks"
        return render(request,'portfolio.html',{'form':form,'message':message})


    
        