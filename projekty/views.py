# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse


def index(request):
    kontekst = {'komunikat': "Witamy w aplikacji Projekty KzK! Tu możesz założyć konto, zalogować się i zgłosić swój projekt. Zapraszamy!"}
    return TemplateResponse(request, 'projekty/index.html', kontekst)

def custom_404(request):
    return render(request, '404.html', {}, status=404)

def custom_500(request):
    return render(request, '500.html', {}, status=500)

@method_decorator(login_required, 'dispatch')
class NazwaCreate(CreateView):
    """Widok dodawania projektów"""
    
    model = models.Nazwa
    form_class = forms.NazwaForm
    success_url = reverse_lazy('projekty:lista')
    
    def nazwa(request):
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Photo(docfile=reques.FILES['docfile'])
                newdoc.save()
                
                return HttpResponseRedirect(reverse('list'))
        else:
            form = PhotoForm()
            
        documents = Photo.objects.all()
        
        return render(
            request,
            'nazwa.html',
            {'documents': documents, 'form': form}
        )


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
    

    
    
#DetailView na później ++++
    
"""
@method_decorator(login_required, 'dispatch')
class NazwaDetailView(DetailView):
    model = models.Nazwa
    
"""





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
