from django.views import generic
from ..models.prices import Prices
from .pageablemixin import PageableMixin
from django.db.models import Q

from ..forms.tradeform import TradeForm
from django.http import HttpResponseRedirect,HttpResponse

from ..lib.datacrawler.pandascrawler import PandasCrawler

from datetime import datetime

import logging

class HistoryGetView(generic.FormView):
    template_name = 'tradeanalyzer/analyze.html'

    form_class = TradeForm

    company_code = '0'

    prices_list = None
    success_url = 'history'
    end_year    = 1999
    end_month   = 1
    end_day     = 1
    
    __debug     = True

    @property
    def debug(self):
        return self.__debug
    
    @debug.setter
    def debug(self, val):
        self.__debug = val

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form, **kwargs)

    def form_invalid(self, form, **kwargs):
        print(__name__, 'form_invalid, ')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context[show_results] = False
        return self.render_to_response(context)

    def form_valid(self, form):
        self.company_code = form.cleaned_data['company_code']
        self.end_year     = int(form.cleaned_data['year'])
        self.end_month    = int(form.cleaned_data['month'])
        self.end_day      = int(form.cleaned_data['day'])

        enddate = datetime(self.end_year,self.end_month, \
                           self.end_day,0,0).strftime('%Y-%m-%d')

        if self.__debug == True:
            print(__name__, 'company_code =', self.company_code)
            print(__name__, 'enddate      =', enddate)

        dataList = PandasCrawler.crawl(companyCode=self.company_code,\
                                       endDate = enddate,\
                                       debug=self.__debug)
        for row in dataList:
            price = Prices(code=row['code'],\
                           price_date  = row['date'],\
                           price_open  = row['open'],\
                           price_close = row['close'],\
                           price_high  = row['high'],\
                           price_low   = row['low'],\
                           volume      = row['volume'])
            if self.__debug == True:
                print(__name__, price)
            price.checkAndSave()
        return HttpResponseRedirect('history/'+str(self.company_code))
