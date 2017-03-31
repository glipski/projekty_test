# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

def index(request):
    kontekst = {'komunikat': "Witamy w aplikacji Projekty KzK!"}
    return TemplateResponse(request, 'projekty/index.html', kontekst)
    
@method_decorator(login_required, 'dispatch')
class NazwaCreate(CreateView):
    """Widok dodawania projektów"""
    
    model = models.Nazwa
    form_class = forms.NazwaForm
    success_url = reverse_lazy('projekty:lista')


@method_decorator(login_required, 'dispatch')
class NazwaUpdate(UpdateView):
    """Widok aktualizuacji"""

    model = models.Nazwa
    form_class = forms.NazwaForm
    success_url = reverse_lazy('projekty:lista')
    
@method_decorator(login_required, 'dispatch')
class NazwaDelete(DeleteView):
    model = models.Nazwa
    success_url = reverse_lazy('projekty:lista') 

"""
    def get_context_data(self, **kwargs):
        context = super(NazwaDelete, self).get_context_data(**kwargs)
        info = models.Nazwa.objects.filter(projekty=self.object)
        context['info'] = info
        return context
""" 


"""
    
    def get_context_data(self, **kwargs):
        context = super(NazwaCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['dane'] = forms.DaneFormSet(self.request.POST)
        else:
            context['dane'] = forms.DaneFormSet()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        dane = forms.DaneFormSet(self.request.POST)
        if form.is_valid() and dane.is_valid():
            return self.form_valid(form, dane)
        else:
            return self.form_invalid(form, dane)

    def form_valid(self, form, dane):
        form.instance.autor = self.request.user
        self.object = form.save()
        dane.instance = self.object
        dame.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, dane):
        return self.render_to_response(
            self.get_context_data(form=form, dane=dane)
        )
    


"""
