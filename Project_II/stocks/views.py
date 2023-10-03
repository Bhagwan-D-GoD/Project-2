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


def porfolio(request):
    
    return render(request,'portfolio.html')