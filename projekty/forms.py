# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea
from . import models
from django.forms.models import inlineformset_factory
from django import forms

class NazwaForm(ModelForm):
    
    class Meta:
        model = models.Nazwa
        exclude = ('data_publikacji', '#')
        zdjecie = forms.FileField(label='Select a file')
        widgets = {'nazwa_projektu': Textarea(attrs={'rows':1, 'cols': 75}),
                   'krotki_opis': Textarea(attrs={'rows':1, 'cols': 75}),
                   'dlugi_opis': Textarea(attrs={'rows':1, 'cols': 75}),
                   'problemy': Textarea(attrs={'rows':1, 'cols': 75}),
                   'bledy': Textarea(attrs={'rows':1, 'cols': 75}),
                   'szkola': Textarea(attrs={'rows':1, 'cols':50}),
                   'liczba_uczniow': Textarea(attrs={'rows':1, 'cols': 75}),
				   'informacje': Textarea(attrs={'rows':2, 'cols':50}),
    
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
