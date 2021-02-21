# from django.forms import Form, ModelForm, inlineformset_factory, BaseInlineFormSet
from django import forms

from .models import Menu, Memo


class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'date', 'category')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


MemoFormset = forms.inlineformset_factory(parent_model=Menu, model=Memo, form=MenuCreateForm,
                                          fields=('memo',), extra=1,)

