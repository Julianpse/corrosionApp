# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from main_app.forms import TechForm
from main_app.forms import CreateEquipmentForm
from main_app.forms import ViewEquipmentData


# Create your views here.
def tech(request):
    args = {'form':TechForm}
    return render(request,'main_app/tech.html',args)

def create_equipment(request):
    args = {'form':CreateEquipmentForm}
    return render(request, 'main_app/create_equipment.html',args)

def view_data(request):
    args = {'form':ViewEquipmentData}
    return render(request, 'main_app/view_data.html',args)
