from django.views import generic
from ..models.prices import Prices

class PricesView(generic.ListView):
    model = Prices 
    template_name = 'tradeanalyzer/prices_list.html'
    context_object_name = 'prices_list'

    def get_queryset(self):
        """Return the last five published questions."""
        #return Prices.objects.filter(
        #    pub_date__lte = timezone.now()
        #).order_by('-pub_date')[:5]
        return Prices.objects.order_by('-id')[:]
