from django import forms
from .models import stockportfolio
class addstockform(forms.ModelForm):
    class Meta:
        model=stockportfolio
        fields=('stocksymbol','stockname','quantity')