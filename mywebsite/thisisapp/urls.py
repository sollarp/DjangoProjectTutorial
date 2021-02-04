from django.urls import path

from . import views

urlpatterns = [
    # ex: /thisisapp/
    path('', views.index, name='index'),
    # ex: /thisisapp/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /thisisapp/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /thisisapp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /thisisapp/5/detail/
    path('<int:question_id>/detail/', views.vote, name='detail'),
]
