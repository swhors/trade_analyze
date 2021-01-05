from django import forms
#from djangotoolbox.fields import ListField

class TradeForm(forms.Form):
    company_code = forms.CharField(label='compay_code')
    year         = forms.CharField(label='year')
    month        = forms.CharField(label='month')
    day          = forms.CharField(label='day')
