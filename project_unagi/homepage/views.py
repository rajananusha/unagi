# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def foo(request):
    return HttpResponse("Hello, world. You're at the Home Page.")
    # return render(request, 'aloha.html')
