# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User



# Create your models here.

@python_2_unicode_compatible
class Nazwa(models.Model):
    nazwa_projektu = models.CharField(max_length=50)
    #data_publikacji = models.DateTimeField('data publikacji', null=False)
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    krotki_opis = models.CharField(max_length=200)
    dlugi_opis = models.CharField(max_length=500)
    problemy = models.CharField(max_length=500)
    bledy = models.CharField(max_length=500)
    szkola = models.CharField(max_length=200)
    liczba_uczniow = models.IntegerField(default=0)
    informacje = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nazwa_projektu
        
    class Meta:
        verbose_name_plural = 'nazwy'
    
"""
@python_2_unicode_compatible
class Dane(models.Model):
    nazwa = models.ForeignKey(Nazwa, on_delete=models.CASCADE)
    opis_projektu = models.CharField(max_length=200)
    szkola = models.CharField(max_length=200)
    liczba_uczniow = models.IntegerField(default=0)
    
    def __str__(self):
        return self.opis_projektu

    class Meta:
        verbose_name_plural = 'dane'
"""
