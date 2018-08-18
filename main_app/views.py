# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'main_app/index.html',context = my_dict)
