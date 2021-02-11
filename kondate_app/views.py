from django.contrib import messages
from django.urls import reverse_lazy
from datetime import date
from django.views.generic import TemplateView, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import CustomUser
from .models import Menu
from .forms import MenuCreateForm


class StartView(TemplateView):
    template_name = 'start.html'


class TodayMenuView(LoginRequiredMixin, ListView):
    template_name = 'today_menu.html'
    model = Menu

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        family_obj = CustomUser.objects.get(username=self.request.user).family
        if not family_obj:
            return context

        today_menu = family_obj.menu_family.filter(date=date.today())

        if not today_menu:
            context["today_menu_blank"] = True

        context["main_dish"] = today_menu.filter(category="main_dish").first()
        context["side_dish"] = today_menu.filter(category="side_dish").first()
        context["soup"] = today_menu.filter(category="soup").first()
        context["rice"] = today_menu.filter(category="rice").first()
        context["dessert"] = today_menu.filter(category="dessert").first()
        context["drink"] = today_menu.filter(category="drink").first()

        return context

    # def get_queryset(self):
    #
    #     family_obj = CustomUser.objects.get(username=self.request.user).family
    #     if not family_obj:
    #         return True
    #
    #     today_menu = family_obj.menu_family.filter(date=date.today())
    #
    #     main_dish = today_menu.filter(category="main_dish").first()
    #     side_dish = today_menu.filter(category="side_dish").first()
    #     soup = today_menu.filter(category="soup").first()
    #     rice = today_menu.filter(category="rice").first()
    #     dessert = today_menu.filter(category="dessert").first()
    #     drink = today_menu.filter(category="drink").first()
    #
    #     query_sets = {
    #         "family_obj": family_obj,
    #         "main_dish": main_dish,
    #         "side_dish": side_dish,
    #         "soup": soup,
    #         "rice": rice,
    #         "dessert": dessert,
    #         "drink": drink,
    #     }
    #     return query_sets


class MenuCreateView(LoginRequiredMixin, CreateView):
    model = Menu
    template_name = "create_menu.html"
    form_class = MenuCreateForm
    success_url = reverse_lazy('kondate_app:today')

    def form_valid(self, form):
        family_obj = CustomUser.objects.get(username=self.request.user).family
        menu = form.save(commit=False)
        menu.family = family_obj
        menu.save()
        messages.success(self.request, "献立を作成しました。")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "献立の作成に失敗しました。")
        return super().form_invalid(form)


class MenuUpdateView(LoginRequiredMixin, UpdateView):
    model = Menu
    template_name = 'update_menu.html'
    form_class = MenuCreateForm
    success_url = reverse_lazy('kondate_app:today')

    def get_success_url(self):
        return reverse_lazy('kondate_app:today', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'レシピを更新しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'レシピの更新に失敗しました')
        return super(self).form_invalid(form)


class MenuDeleteView(LoginRequiredMixin, DeleteView):
    model = Menu
    template_name = 'delete_menu.html'
    success_url = reverse_lazy('kondate_app:today')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "献立を削除しました")
        return super().delete(request, *args, **kwargs)














