from django import forms

from kondate_app.models import Menu, MenuIngredient


class MenuCreateForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ('name', 'date', 'category')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


MenuIngredientFormset = forms.inlineformset_factory(
    parent_model=Menu,
    model=MenuIngredient,
    form=MenuCreateForm,
    fields=('name', 'amount'),
    extra=1,
)
