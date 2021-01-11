from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class StartView(generic.TemplateView):
    template_name = 'start.html'


class IndexView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'index.html'
