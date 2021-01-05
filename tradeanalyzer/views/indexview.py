from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic

from ..models.codes import Codes

class IndexView(generic.TemplateView):
    template_name = 'tradeanalyzer/index.html'
    #context_object_name = 'latest_question_list'
    
    #def get_queryset(self):
    #    """Return the last five published questions."""
    #    return Question.objects.filter(
    #        pub_date__lte = timezone.now()
    #    ).order_by('-pub_date')[:5]

