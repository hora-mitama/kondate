from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, UpdateView

from accounts.models import CustomUser
from .models import Recipe
from .forms import RecipeCreateForm, RecipeIngredientFormset


class StartView(TemplateView):
    template_name = 'start.html'


@login_required()
def today_list(request):
    family_obj = CustomUser.objects.get(username=request.user).family
    if not family_obj:
        family_is_blank = True
        return render(request, 'today_recipe.html', {'family_is_blank': family_is_blank})

    today_recipe = family_obj.recipe_family.filter(date=timezone.now())
    if not today_recipe:
        today_recipe_is_blank = True
        return render(request, 'today_recipe.html', {'today_recipe_is_blank': today_recipe_is_blank})

    main_dish = today_recipe.filter(category="main_dish").first()
    side_dish = today_recipe.filter(category="side_dish").first()
    soup = today_recipe.filter(category="soup").first()
    rice = today_recipe.filter(category="rice").first()
    dessert = today_recipe.filter(category="dessert").first()
    drink = today_recipe.filter(category="drink").first()

    return render(request, 'today_recipe.html', {
        'main_dish': main_dish,
        'side_dish': side_dish,
        'soup': soup,
        'rice': rice,
        'dessert': dessert,
        'drink': drink,
    })


@login_required()
def create(request):

    form = RecipeCreateForm(request.POST, request.FILES)
    family_obj = CustomUser.objects.get(username=request.user).family

    if request.method == 'POST' and form.is_valid():
        recipe = form.save(commit=False)
        recipe.family = family_obj

        ingredient_formset = RecipeIngredientFormset(request.POST, instance=recipe)

        if ingredient_formset.is_valid():
            recipe.save()
            ingredient_formset.save()
            message = messages.success(request, "献立を作成しました。")
            return redirect('kondate_app:today')
        else:
            formset_error = ingredient_formset.errors
            context = {
                'formset_error': formset_error,
                'form': form,
                'ingredient_formset': ingredient_formset,
            }
    else:
        form_error = form.errors
        context = {
            'form_error': form_error,
            'form': form,
            'ingredient_formset': RecipeIngredientFormset(),
        }

    return render(request, 'create_recipe.html', context)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = 'update_Recipe.html'
    form_class = RecipeCreateForm
    success_url = reverse_lazy('kondate_app:today')

    def get_success_url(self):
        return reverse_lazy('kondate_app:today', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'レシピを更新しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'レシピの更新に失敗しました')
        return super(self).form_invalid(form)


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'delete_Recipe.html'
    success_url = reverse_lazy('kondate_app:today')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "献立を削除しました")
        return super().delete(request, *args, **kwargs)

