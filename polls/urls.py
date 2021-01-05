from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('index1/', views.index, name='index1'),
    path('',views.IndexView.as_view(),name='index'),
    path('<int:question_id>/', views.detail, name='detail1'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/results/', views.results, name='results1'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
