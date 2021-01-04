from django.shortcuts import render
from django.views import generic


class StartView(generic.TemplateView):
    template_name = 'start.html'


class IndexView(generic.TemplateView):
    template_name = 'index.html'
