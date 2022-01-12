from django.urls import re_path, include
from django.views.generic import TemplateView

from mysite.books import views

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    re_path(r'^books/$', views.book_list, name='book_list'),
    re_path(r'^books/create/$', views.book_create, name='book_create'),
    re_path(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    re_path(r'^books/(?P<pk>\d+)/delete/$', views.book_delete, name='book_delete'),
]
