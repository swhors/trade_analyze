from django.views import generic
from ..models.prices import Prices
from .pageablemixin import PageableMixin
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect, csrf_exempt #, never_cache

from ..forms.tradeform import TradeForm
from ..forms.tradeformctl import TradeCtlDelForm
from django.http import HttpResponseRedirect,HttpResponse#, HttpRedirect
from django.shortcuts import redirect

from ..lib.datacrawler.pandascrawler import PandasCrawler

from datetime import datetime

from mysite.settings import CSRF_COOKIE_NAME
import mysite.settings

import logging

#from django.core.urlresolvers import reverse
from django.shortcuts import resolve_url
from ast import literal_eval

class HistoryCtlView(generic.FormView):
    template_name = 'tradeanalyzer/analyze.html'

    form_class = TradeCtlDelForm

    company_code = '0'

    price_list = None
    success_url = '/trade/history'
    end_year    = 1999
    end_month   = 1
    end_day     = 1
    
    __debug     = False

    def __init__(self):
        print(__name__, 'init')
        print(__name__, CSRF_COOKIE_NAME)

    @property
    def debug(self):
        return self.__debug
    
    @debug.setter
    def debug(self, val):
        self.__debug = val

    def post(self, request, *args, **kwargs):
        print(__name__, CSRF_COOKIE_NAME)
        form = self.form_class(request.POST)
        #print('success_url ={}'%(request.POST.success_url))
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form, **kwargs)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def form_valid(self, form):
        if self.__debug==True:
            print("company_code val =", self.company_code)

        self.company_code = form.cleaned_data['company_code']
        self.price_list = form.cleaned_data['price_list']
        
        if self.price_list != None:
            price_dict = literal_eval(self.price_list)
            if price_dict != None:
                prices = Prices()
                for price in price_dict:
                    print(__name__, 'price == ', price)
                    prices.deleteItem(self.company_code, price['price_date'])
            
        else:
            print(__name__, 'Price is not selected.')
        return HttpResponseRedirect('history/'+self.company_code)
