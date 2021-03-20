from django.forms import ModelForm
from colors_app.widgets import ColorChannelRangeInput
from colors_app.models import Color
from random import randint

class ColorForm(ModelForm):
    class Meta:
        model = Color
        fields = ['name', 'red', 'green', 'blue']
        widgets = {
            'red': ColorChannelRangeInput(),
            'green': ColorChannelRangeInput(),
            'blue': ColorChannelRangeInput(),
        }
