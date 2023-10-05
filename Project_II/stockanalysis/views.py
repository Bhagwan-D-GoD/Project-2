# views.py
from django.shortcuts import render
import plotly.graph_objs as go
import yfinance as yf
from .utils import get_plot

def chart_view(request):
    x_data = ['January', 'February', 'March', 'April', 'May']
    y_data = [65, 59, 80, 81, 56]

    # Create a Plotly figure
    fig = go.Figure(data=[go.Bar(x=x_data, y=y_data)])

    # Convert the figure to HTML
    chart_div = fig.to_html(full_html=False)
    return render(request, 'chart.html', {'chart_div': chart_div})










#######################################
def main_view(request):
    df=yf.download('AAPL',start = '2022-12-01',end = '2022-12-31')
    x=[x.close for x in df]
    y=[y.date for y in df]
    graph=get_plot(x,y)
    return render(request,'graph.html',{'graph':graph})


