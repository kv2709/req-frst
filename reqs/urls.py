"""Set URL for reqs"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page for work phone-dealer
    url(r'^$', views.index, name='index'),
    # work page for create request for forsto.ru
    url(r'^work_page/$', views.work_page, name='work_page'),
    # Page with result request
    url(r'^res_req$', views.res_req, name='res_req'),
    # About page
    url(r'^about$', views.about, name='about'),

]
