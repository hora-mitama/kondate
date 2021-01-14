from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class StartView(TemplateView):
    template_name = 'start.html'


class IndexView(TemplateView, LoginRequiredMixin):
    template_name = 'index.html'
