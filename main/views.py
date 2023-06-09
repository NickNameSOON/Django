from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import Form


def forms(request):
    context = {}
    if request.method == 'post':
        pass
    else:
        form = Form()
    return render(request, 'main/forms.html')


def about(request):
    return render(request, 'main/about.html')


def index(request):
    return render(request, 'main/index.html')


