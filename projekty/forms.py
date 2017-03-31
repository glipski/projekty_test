# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory

class NazwaForm(ModelForm):
    
    class Meta:
        model = models.Nazwa
        exclude = ('data_publikacji', '#')
        widgets = {'opis_projektu': Textarea(attrs={'rows':2, 'cols': 50}),
				   'szkola': Textarea(attrs={'rows':2, 'cols':50}),
				   'nazwa_projektu': Textarea(attrs={'rows':2, 'cols':50}),
				   
				   
				  
				
        
        
        }
        
"""
DaneFormSet = inlineformset_factory(
    parent_model=models.Nazwa,
    model=models.Dane,
    validate_max=True,
    validate_min=True,
    max_num=10,
    min_num=1,
    fields=('nazwa', 'opis_projektu', 'szkola', 'liczba_uczniow')
    
)
"""
