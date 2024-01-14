from django.shortcuts import render

from random import random
from datetime import datetime

from django.views import View
from django.http import HttpResponse

class CurrentDateView(View):
    def get(self, request):
        html = f'{datetime.now()}'
        return HttpResponse(html)

class RandView(View):
    def get(self, request):
        random_number = random()
        return HttpResponse(random_number)

class Hello(View):
    def get(self, request):
        a = "<h1>Hello, World</h1>"
        return HttpResponse(a)

class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')