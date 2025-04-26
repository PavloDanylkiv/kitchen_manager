from django.views.generic import TemplateView

from restaurant.models import DishType, Cook, Dish


class IndexView(TemplateView):
    template_name = "restaurant/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["num_dish_type"] = DishType.objects.count()
        context["num_cook"] = Cook.objects.count()
        context["num_dish"] = Dish.objects.count()
        return context
