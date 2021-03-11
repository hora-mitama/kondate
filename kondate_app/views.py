from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, UpdateView

from accounts.models import CustomUser
from .models import Recipe
from .forms import RecipeCreateForm, RecipeIngredientFormset, RecipeProcessFormset


class StartView(TemplateView):
    template_name = 'start.html'


def paginate_queryset(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


@login_required()
def recipe_list(request):
    user = get_object_or_404(CustomUser, username=request.user)
    obj_list = user.recipe_user.all()
    posts = paginate_queryset(request, obj_list, 10)

    return render(request, 'recipe_list.html', {'posts': posts})


@login_required()
def today_menu_list(request):
    user_obj = get_object_or_404(CustomUser, username=request.user)
    recipe_obj = user_obj.recipe_user.all()
    if not recipe_obj:
        recipe_is_blank = True
        return render(request,
                      'today_menu.html',
                      {'recipe_is_blank': recipe_is_blank})

    today_menu = recipe_obj.menu_recipe.filter(date=timezone.now())

    main_dish = today_menu.filter(category="main_dish").first()
    side_dish = today_menu.filter(category="side_dish").first()
    soup = today_menu.filter(category="soup").first()
    rice = today_menu.filter(category="rice").first()
    dessert = today_menu.filter(category="dessert").first()
    drink = today_menu.filter(category="drink").first()

    return render(request,
                  'today_menu.html',
                  {
                      'main_dish': main_dish,
                      'side_dish': side_dish,
                      'soup': soup,
                      'rice': rice,
                      'dessert': dessert,
                      'drink': drink,
                  })


@login_required()
def recipe_create(request):
    form = RecipeCreateForm(request.POST, request.FILES)

    if request.method == 'POST' and form.is_valid():
        recipe = form.save(commit=False)
        recipe.user = request.user

        ingredient_formset = RecipeIngredientFormset(request.POST, instance=recipe)
        process_formset = RecipeProcessFormset(request.POST, instance=recipe)

        if ingredient_formset.is_valid() and process_formset.is_valid():
            recipe.save()
            ingredient_formset.save()
            process_formset.save()
            message = messages.success(request, "献立を作成しました。")
            return redirect('kondate_app:today')
        else:
            formset_error = ingredient_formset.errors
            context = {
                'formset_error': formset_error,
                'form': form,
                'ingredient_formsets': ingredient_formset,
                'process_formsets': process_formset,
            }
    else:
        form_error = form.errors
        context = {
            'form_error': form_error,
            'form': form,
            'ingredient_formsets': RecipeIngredientFormset(),
            'process_formsets': RecipeProcessFormset(),
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

# @login_required()
# def today_list(request):
#     family_obj = CustomUser.objects.get(username=request.user).family
#     if not family_obj:
#         family_is_blank = True
#         return render(request, 'today_menu.html', {'family_is_blank': family_is_blank})
#
#     today_menu = family_obj.recipe_family.filter(date=timezone.now())
#     if not today_menu:
#         today_menu_is_blank = True
#         return render(request, 'today_menu.html', {'today_menu_is_blank': today_menu_is_blank})
#
#     main_dish = today_menu.filter(category="main_dish").first()
#     side_dish = today_menu.filter(category="side_dish").first()
#     soup = today_menu.filter(category="soup").first()
#     rice = today_menu.filter(category="rice").first()
#     dessert = today_menu.filter(category="dessert").first()
#     drink = today_menu.filter(category="drink").first()
#
#     return render(request, 'today_menu.html', {
#         'main_dish': main_dish,
#         'side_dish': side_dish,
#         'soup': soup,
#         'rice': rice,
#         'dessert': dessert,
#         'drink': drink,
#     })
