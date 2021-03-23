from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy
from colors_app.models import Color
from colors_app.forms import ColorForm
from django.conf import settings

class ColorListView(ListView):
    model = Color
    template_name = "colors_app/color_list.html"
    queryset = Color.objects.order_by("name")

class NewColorView(CreateView):
    model = Color
    form_class = ColorForm
    template_name = "colors_app/color_form.html"
    success_url = reverse_lazy("colors_app:color_list")

class ColorDetailView(DetailView):
    model = Color
    template_name = "colors_app/color_detail.html"

    def get_context_data(self, *args, **kwargs):
        "Adds properties to the context dict sent to the template"
        context = super().get_context_data(*args, **kwargs)
        color = self.get_object()
        hues = []
        for adjustment in settings.HUES_TO_SHOW:
            if adjustment == 0:
                hues.append(color)
            else:
                hue = color.adjust_hue(adjustment)
                hue.name = hue.hex_code()
                hues.append(hue)
        context['color'] = color
        context['hues'] = hues
        return context
