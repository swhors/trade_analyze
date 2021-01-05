from django.views import generic
from ..models.prices import Prices
from .pageablemixin import PageableMixin
from django.db.models import Q

from datetime import datetime
from .datepicker import DatePicker
import logging

class HistoryView(generic.ListView, DatePicker):
    model = Prices 
    logger = logging.getLogger(__name__)
    template_name = 'tradeanalyzer/prices_list.html'
    context_object_name = 'prices_list'
    paginate_by = 20
    company_code = '0'
    
    def __init__(self):
        DatePicker.__init__(self)

    def get_queryset(self):
        if 'company_code' in self.kwargs.keys():
            self.company_code = self.kwargs['company_code']
        else:
            self.company_code = '0'
        prices = Prices.objects.filter(code=self.company_code)
        return prices
    
    def get_context_data(self, **kwargs):        
        context = super(HistoryView, self).get_context_data(**kwargs)
        context['company_code'] = self.company_code
        context['prices_list']  = self.get_queryset
        DatePicker.__now__(self, context)

        paginator = context['paginator']

        page_numbers_range = 5 # Dispaly only 5 page numbers
        max_index = len(paginator.page_range)
        page = self.request.GET.get('page')
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        return context

def delete_test(request):
    if request.is_ajax():
        selected_tests = request.POST['test_list_ids']
        selected_tests = json.loads(selected_tests)
        for i, test in enumerate(selected_tests):
            if test != '':
                Test.objects.filter(id__in=selected_tests).delete()
    return HttpResponseRedirect('/test-management/test/')
