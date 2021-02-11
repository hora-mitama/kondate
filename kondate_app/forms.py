from django.forms import ModelForm

from .models import Menu


class MenuCreateForm(ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'date', 'category',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
