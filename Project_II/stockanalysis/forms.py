from django import forms

class searchform(forms.Form):
    min_price = forms.DecimalField(label='Minimum Price', required=False)
    max_price = forms.DecimalField(label='Maximum Price', required=False)
    min_pe_ratio = forms.DecimalField(label='P/E Ratio', required=False)
    max_pe_ratio = forms.DecimalField(label='P/E Ratio', required=False)
    min_pb_ratio=forms.DecimalField(label='P/B Ratio',required=False)
    max_pb_ratio=forms.DecimalField(label='P/B Ratio',required=False)