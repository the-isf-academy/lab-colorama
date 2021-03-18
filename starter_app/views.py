from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView, UpdateView, TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'starter_app/indexView.html'

