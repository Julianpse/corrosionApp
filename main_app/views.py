# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from RESTapi.models import FixedEquipment, Facility, Measurements, TmlInfo


# Create your views here.
def home(request):
    args = {}
    return render(request,'main_app/home.html', args)

def tech(request):
    equipment_name = FixedEquipment.objects.all()
    facility = Facility.objects.all()
    tml = TmlInfo.objects.all()

    args = {'equipment_name': equipment_name, 'facility':facility, 'tml':tml}
    return render(request,'main_app/tech.html',args)

def create_equipment(request):
    args = {}
    return render(request, 'main_app/create_equipment.html',args)

def view_data(request):
    args = {}
    return render(request, 'main_app/view_data.html',args)
