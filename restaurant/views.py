from django.contrib.auth.mixins import LoginRequiredMixin
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
    CookCreateForm,
)
from restaurant.models import DishType, Cook, Dish


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "restaurant/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["num_dish_type"] = DishType.objects.count()
        context["num_cook"] = Cook.objects.count()
        context["num_dish"] = Dish.objects.count()
        return context


class CookListView(LoginRequiredMixin, generic.ListView):
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


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreateForm
    success_url = reverse_lazy("restaurant:index")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("restaurant:cook-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "restaurant/cook_confirm_delete.html"
    success_url = reverse_lazy("restaurant:cook-list")


class DishListView(LoginRequiredMixin, generic.ListView):
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


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishUpdateForm
    success_url = reverse_lazy("restaurant:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishUpdateForm
    success_url = reverse_lazy("restaurant:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "restaurant/dish_confirm_delete.html"
    success_url = reverse_lazy("restaurant:dish-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.select_related().prefetch_related()


class DishTypeListView(LoginRequiredMixin, generic.ListView):
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


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeUpdateForm
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "restaurant/dishtype_confirm_delete.html"
    success_url = reverse_lazy("restaurant:dish-type-list")
