from django.views import generic
from ..models.codes import Codes
from ..models.prices import Prices
from ..forms.tradeform import TradeForm
from django.http import HttpResponseRedirect,HttpResponse


class AnalyzeFinishView(generic.TemplateView):
    template_name = 'tradeanalyzer/analyze.html'

    form_class = TradeForm

    company_code = '0'

    prices_list = None
    #sucess_url = '.'

    #def get_queryset(self):
    #    self.company_code = str(self.kwargs['company_code'])
    #    return Prices.object.filter(code=compnay_code)
    
    #def get(self, request, *args, **kwargs):
    #   company_code = str(request.GET.get('company_code', ''))
    #   print('company_code = ' + company_code)
    #   self.prices_list = Prices.objects.filter(code=company_code)
    #   #return super().get(request, *args, **kwargs)
    #   return "success";

    def __init__(self):
        #self.company_code = str(self.kwargs['company_code'])
        None

    def get_context_data(self, **kwargs):
        context = super(AnalyzeFinishView, self).get_context_data(**kwargs)
        #self.company_code = str(self.request.POST.post('company_code'))
        #prices_num = Prices.objects.count()
        #context['data'] = {'prices_num':prices_num}
        #context['company_code'] = self.company_code
        return context
