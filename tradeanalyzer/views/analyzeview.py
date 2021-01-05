from django.views import generic
from ..models.codes import Codes
from ..models.prices import Prices
from ..forms.tradeform import TradeForm
from django.http import HttpResponseRedirect,HttpResponse

from ..lib.executor import Executor


#class AnalyzeView(generic.FormView):
#    template_name = 'tradeanalyzer/analyze.html'
class AnalyzeView(generic.TemplateView):
    template_name = 'tradeanalyzer/analyze.html'

    form_class = TradeForm

    company_code = '0'

    prices_list = None
    #success_url = 'analyzefinish'
    return_url  = None
    end_year    = 1999
    end_month   = 1
    end_day     = 1

    debug       = True

    #def get_queryset(self):
    #    self.company_code = str(self.kwargs['company_code'])
    #    return Prices.object.filter(code=compnay_code)
    
    #def get(self, request, *args, **kwargs):
    #   company_code = str(request.GET.get('company_code', ''))
    #   print('company_code = ' + company_code)
    #   self.prices_list = Prices.objects.filter(code=company_code)
    #   #return super().get(request, *args, **kwargs)
    #   return "success";

    #def form_valid(self, form):
    #    return super(AnalyzeVie, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if self.debug == True:
            print(__name__, 'form = ' , str(form))

        if form.is_valid():
            print('type of cleaned_data = ', type(form.cleaned_data))
            self.company_code = form.cleaned_data['company_code']
            if 'return_url' in form.cleaned_data:
                self.return_url   = form.cleaned_data['return_url']
            self.end_year     = form.cleaned_data['year']
            self.end_month    = form.cleaned_data['month']
            self.end_day      = form.cleaned_data['day']
            enddate = '{:04d}{:02d}{:02d}'.format(int(self.end_year), int(self.end_month), int(self.end_day))
            if self.debug == True:
                print(__name__, 'post, company_code =' , self.company_code)
                print(__name__, 'post, enddate      =' , enddate        )
            Executor.analyze(self.company_code, enddate)
            return form
            # return HttpResponseRedirect('analyzefinish?company_code=' + \
            #                             self.company_code + \
            #                             '&' + \
            #                             'enddate=' + \
            #                             enddate)

    def get_context_data(self, **kwargs):
        print(__name__, 'get_context, 0')
        context = super(AnalyzeView, self).get_context_data(**kwargs)
        print(__name__, 'get_context, 1')
        self.company_code = str(self.request.POST.post('company_code'))
        print(__name__, 'get_context, 2')
        
        Executor.analyze(self.company_code)
        print(__name__, 'get_context, 3')

        prices_num = Prices.objects.count()
        print(__name__, 'get_context, 4')
        context['data'] = {'prices_num':prices_num}
        context['company_code'] = self.company_code
        context['year'] = self.end_year
        context['month'] = self.end_month
        context['day'] = self.end_day
        return context
