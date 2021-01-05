from django import forms
#from djangotoolbox.fields import ListField

class TradeCtlDelForm(forms.Form):
    company_code = forms.CharField(label='compay_code')
    price_list    = forms.CharField(label='price_list')
    year         = forms.CharField(label='year')
    month        = forms.CharField(label='month')
    day          = forms.CharField(label='day')
