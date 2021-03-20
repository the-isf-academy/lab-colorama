from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy
from colors_app.models import Color
from colors_app.forms import ColorForm

class ColorListView(ListView):
    model = Color
    template_name = "colors_app/color_list.html"
    queryset = Color.objects.order_by("name")

class NewColorView(CreateView):
    model = Color
    form_class = ColorForm
    template_name = "colors_app/color_form.html"
    success_url = reverse_lazy("colors_app:color_list")
