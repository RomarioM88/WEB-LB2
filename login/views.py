from django.shortcuts import render

from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse

class LoginView(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        return JsonResponse(request.POST, json_dumps_params={"indent": 4})

