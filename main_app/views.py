# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from main_app.forms import HomeForm


# Create your views here.
def home(request):
    args = {'form':HomeForm}
    return render(request,'main_app/home.html',args)
