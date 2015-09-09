from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /local1000/
    url(r'^$', views.index, name='index'),
    url(r'^urls1000/$', views.urls1000),
    url(r'^repertory/(?P<rep_id>[0-9]+)/$', views.repertory),
    url(r'^picIndexAjax/$', views.pic_index_ajax),
    url(r'^picContentAjax/$', views.pic_content_ajax),
    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
