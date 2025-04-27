from django.views import generic
from django.views.generic import TemplateView

from restaurant.forms import CookSearchForm
from restaurant.models import DishType, Cook, Dish


class IndexView(TemplateView):
    template_name = "restaurant/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["num_dish_type"] = DishType.objects.count()
        context["num_cook"] = Cook.objects.count()
        context["num_dish"] = Dish.objects.count()
        return context


class CookListView(generic.ListView):
    model = Cook
    template_name = "restaurant/cook_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        username = self.request.GET.get("username")
        if username:
            return queryset.filter(username__icontains=username)
        return queryset
