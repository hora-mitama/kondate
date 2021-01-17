from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Menu, Family


class StartView(TemplateView):
    template_name = 'start.html'


class IndexView(TemplateView, LoginRequiredMixin):
    template_name = 'index.html'
    model = Family


class MenuList(ListView):
    template_name = 'list.html'
    model = Menu
