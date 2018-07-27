# Create your views here.
from django.shortcuts import render


def home(request):
    context = locals()
    template = "./profiles/index.html"
    return render(request, template, context)


def about(request):
    context = locals()
    template = "./profiles/about.html"
    return render(request, template, context)
