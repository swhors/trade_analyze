import logging 

class PageableMixin(object):
    logger = logging.getLogger(__name__)
    paginate_by = 10
    block_size = 10

    def get_context_data(self, **kwargs):
        self.logger.debug('PageableMixin.get_context_data()')
        context = super(PageableMixin, self).get_context_data(**kwargs)

        start_index = int((context['page_obj'].number - 1) / self.block_size) * self.block_size
        end_index = min(start_index + self.block_size, len(context['paginator'].page_range))

        context['page_range'] = context['paginator'].page_range[start_index:end_index]

        return context
