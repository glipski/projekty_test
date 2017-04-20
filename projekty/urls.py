# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from . import views
from .models import Nazwa
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from django.contrib import admin
from django.conf import settings


from django.views.generic import DeleteView, DetailView

app_name = 'projekty'

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^lista/', login_required(ListView.as_view(model=Nazwa)),
               name='lista'),
               url(r'^dodaj/$', views.NazwaCreate.as_view(), name='dodaj'),
               url(r'^edytuj/(?P<pk>\d+)/', views.NazwaUpdate.as_view(), name='edytuj'),
               url(r'^usun/(?P<pk>\d+)/', views.NazwaDelete.as_view(), name='usun'),
               #url(r'^info/(?P<pk>\d+)/', views.NazwaDetail.as_view(), name='info'),
              
]




