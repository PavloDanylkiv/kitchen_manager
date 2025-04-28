from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from restaurant.forms import (
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm,
    DishTypeUpdateForm,
    CookUpdateForm,
    DishUpdateForm,
)
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


class CookDetailView(generic.DetailView):
    model = Cook


class CookUpdateView(generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("restaurant:cook-list")


class CookDeleteView(generic.DeleteView):
    model = Cook
    template_name = "restaurant/cook_confirm_delete.html"
    success_url = reverse_lazy("restaurant:cook-list")


class DishListView(generic.ListView):
    model = Dish
    template_name = "restaurant/dish_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.all()
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishUpdateForm
    success_url = reverse_lazy("restaurant:dish-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    form_class = DishUpdateForm
    success_url = reverse_lazy("restaurant:dish-list")


class DishDeleteView(generic.DeleteView):
    model = Dish
    template_name = "restaurant/dish_confirm_delete.html"
    success_url = reverse_lazy("restaurant:dish-list")


class DishDetailView(generic.DetailView):
    model = Dish
    queryset = Dish.objects.select_related().prefetch_related()


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        name = self.request.GET.get("name")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class DishTypeDetailView(generic.DetailView):
    model = DishType


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    form_class = DishTypeUpdateForm
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    template_name = "restaurant/dishtype_confirm_delete.html"
    success_url = reverse_lazy("restaurant:dish-type-list")
