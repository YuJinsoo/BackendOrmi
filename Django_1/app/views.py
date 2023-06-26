from django.shortcuts import render
from django.views import View
from django.urls import reverse

def index(request):
    return render(request, 'index.html')


class IndexMain(View):
    def get(self, request):
        return render(request, 'index.html')
        