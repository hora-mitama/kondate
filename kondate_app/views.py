from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, UpdateView

from accounts.models import CustomUser
from .models import Menu
from .forms import MenuCreateForm, MenuIngredientFormset


class StartView(TemplateView):
    template_name = 'start.html'


@login_required()
def today_list(request):
    family_obj = CustomUser.objects.get(username=request.user).family
    if not family_obj:
        family_is_blank = True
        return render(request, 'today_menu.html', {'family_is_blank': family_is_blank})

    today_menu = family_obj.menu_family.filter(date=timezone.now())
    if not today_menu:
        today_menu_is_blank = True
        return render(request, 'today_menu.html', {'today_menu_is_blank': today_menu_is_blank})

    main_dish = today_menu.filter(category="main_dish").first()
    side_dish = today_menu.filter(category="side_dish").first()
    soup = today_menu.filter(category="soup").first()
    rice = today_menu.filter(category="rice").first()
    dessert = today_menu.filter(category="dessert").first()
    drink = today_menu.filter(category="drink").first()

    return render(request, 'today_menu.html', {
        'main_dish': main_dish,
        'side_dish': side_dish,
        'soup': soup,
        'rice': rice,
        'dessert': dessert,
        'drink': drink,
    })


@login_required()
def create(request):

    form = MenuCreateForm(request.POST or None)
    family_obj = CustomUser.objects.get(username=request.user).family

    if request.method == 'POST' and form.is_valid():
        menu = form.save(commit=False)
        menu.family = family_obj

        ingredient_formset = MenuIngredientFormset(request.POST, instance=menu)

        if ingredient_formset.is_valid():
            menu.save()
            ingredient_formset.save()
            message = messages.success(request, "献立を作成しました。")
            return redirect('kondate_app:today')
        else:
            context = {
                'form': form,
                'ingredient_formset': ingredient_formset,
            }
    else:
        context = {
            'form': form,
            'ingredient_formset': MenuIngredientFormset(),

        }

    return render(request, 'create_menu.html', context)


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

