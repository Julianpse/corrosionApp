# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from RESTapi.models import FixedEquipment, Facility, Measurements, TmlInfo


# Create your views here.
def home(request):
    args = {}
    return render(request,'main_app/home.html', args)

# class TechView(TemplateView):
#     template_name = 'main_app/tech.html'
#
#     def get(self, request):
#         equipment_name = FixedEquipment.objects.all()
#         facility = Facility.objects.all()
#         tml = TmlInfo.objects.all()
#         return render(request,'main_app/tech.html')
#
#     def post(self, request):
#         data = {'facility': facility, 'equipment' : equipment,'tml' : tml}
#         r = requests.post(url = '/submitted', data = data)

def tech(request):
    equipment_name = FixedEquipment.objects.all()
    facility = Facility.objects.all()
    tml = TmlInfo.objects.all()
    for tml in tml:
        tmlDict = dict({tml.id : tml})

    args = {'equipment_name': equipment_name, 'facility':facility, 'tml':tml}
    return render(request,'main_app/tech.html',args)

def create_equipment(request):
    args = {}
    return render(request, 'main_app/create_equipment.html',args)

def view_data(request):
    facility = Facility.objects.all()
    tml = TmlInfo.objects.all()
    equipment_name = FixedEquipment.objects.all()
    args = {'equipment_name': equipment_name, 'facility': facility, 'tml':tml}
    return render(request, 'main_app/view_data.html',args)

