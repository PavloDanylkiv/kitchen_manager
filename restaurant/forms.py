from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

from restaurant.models import DishType, Cook, Dish, Ingredient


class CookSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class CookUpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = Cook
        fields = (
            "first_name",
            "last_name",
            "username",
            "years_of_experience",
        )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class DishUpdateForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class DishTypeUpdateForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"
