from django.shortcuts import render
from datetime import date
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import CustomUser


class StartView(TemplateView):
    template_name = 'start.html'


class TodayMenuView(LoginRequiredMixin, ListView):
    template_name = 'today_menu.html'

    def get_queryset(self):

        family_obj = CustomUser.objects.get(username=self.request.user).family
        if not family_obj:
            return True

        today_menu = family_obj.menu_family.filter(date=date.today())

        main_dish = today_menu.filter(category="main_dish").first()
        side_dish = today_menu.filter(category="side_dish").first()
        soup = today_menu.filter(category="soup").first()
        rice = today_menu.filter(category="rice").first()
        dessert = today_menu.filter(category="dessert").first()
        drink = today_menu.filter(category="drink").first()

        context = {
            "family_obj": family_obj,
            "main_dish": main_dish,
            "side_dish": side_dish,
            "soup": soup,
            "rice": rice,
            "dessert": dessert,
            "drink": drink,
        }
        return


class MenuCreateView(CreateView):
    pass


class MenuList(ListView):
    template_name = 'list.html'
