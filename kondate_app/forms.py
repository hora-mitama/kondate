from django import forms

from kondate_app.models import Recipe, RecipeIngredient


class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'date', 'image', 'category', )
        # exclude = ('family',)

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields[0].widget.attrs["class"] = "name_field"


RecipeIngredientFormset = forms.inlineformset_factory(
    parent_model=Recipe,
    model=RecipeIngredient,
    form=RecipeCreateForm,
    fields=('name', 'amount'),
    extra=1,
    can_delete=False,
)
