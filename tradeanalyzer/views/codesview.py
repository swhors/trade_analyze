from django.views import generic
from ..models.codes import Codes
from .pageablemixin import PageableMixin
from django.db.models import Q

import enum
import logging

class FilterType(enum.Enum):
    NONE    = 0
    BY_NAME = 1
    BY_CODE = 2
    
class CodesView(generic.ListView):
    model = Codes
    logger = logging.getLogger(__name__)
    template_name = 'tradeanalyzer/codes_list.html'
    context_object_name = 'codes_list'
    paginate_by = 20

    keyword = ''

    filter_type = FilterType.NONE

    def get_filter_type(self):
        if self.filter_type == FilterType.NONE:
            return "0"
        elif self.filter_type == FilterType.BY_NAME:
            return "1"
        elif self.filter_type == FilterType.BY_CODE:
            return "2"
        return "0"

    def get_keyword(self):
        if self.keyword == None:
            return ""
        return str(self.keyword)

    def get_queryset_all(self, keyword):
        return Codes.objects.order_by('-id')

    def get_queryset_byname(self, keyword):
        return Codes.objects.filter(
            Q(company__icontains = keyword)
        ).order_by('-id')

    def get_queryset_bycode(self, keyword):
        return Codes.objects.filter(code=str(keyword))

    def strToFilterType(self, typeStr):
        if typeStr == None or typeStr == '0':
            return FilterType.NONE
        elif typeStr == '1':
            return FilterType.BY_NAME
        else:
            return FilterType.BY_CODE

    def get_queryset(self):
        filterType = self.request.GET.get('search_type')
        self.keyword    = self.request.GET.get('key_word')

        self.filter_type = self.strToFilterType(filterType)

        filters = { FilterType.NONE.value:self.get_queryset_all,
                    FilterType.BY_NAME.value:self.get_queryset_byname,
                    FilterType.BY_CODE.value:self.get_queryset_bycode }

        return filters[self.filter_type.value](str(self.keyword))
    
    def get_context_data(self, **kwargs):
        context = super(CodesView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5 # Dispaly only 5 page numbers
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1
        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range

        #print('start_index =%d, end_index = %d'%(start_index, end_index))

        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        context['keyword'] = self.get_keyword
        context['search_type'] = self.get_filter_type
        return context

    #def get_paginate_by(self, queryset):
    #    self.logger.info('CodesView.get_pagenate_by()')
    #    return self.paginate_by
