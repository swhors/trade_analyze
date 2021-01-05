from django.urls import path
  
from . import views
from .views import indexview, codesview, pricesview, historyview, analyzeview, analyzefinishview, analyzefailview, historygetview, historyctlview

app_name = 'tradeanalyzer'

urlpatterns = [
    path('',indexview.IndexView.as_view(),name='index'),
    path('historydelete', historyctlview.HistoryCtlView.as_view(), name='historyctl'),
    path('history/<company_code>',historyview.HistoryView.as_view(),name='history'),
    path('historyget',historygetview.HistoryGetView.as_view(),name='historyget'),
    path('codes/',codesview.CodesView.as_view(),name='codes'),
    path('prices',pricesview.PricesView.as_view(),name='prices'),
    path('analyze',analyzeview.AnalyzeView.as_view(),name='analyze'),
    path('analyzefinish',analyzefinishview.AnalyzeFinishView.as_view(),name='analyzefinish'),
    path('analyzefail',analyzefailview.AnalyzeFailView.as_view(),name='analyzefail'),
]
