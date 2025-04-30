from django.test import TestCase
from django import forms

from restaurant.forms import (
    CookCreateForm,
    CookUpdateForm,
    DishUpdateForm,
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm,
)


class FormsTests(TestCase):
    def test_cook_creation_form_with_years_of_experience_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "Test first",
            "last_name": "Test last",
            "email": "test@test.com",
            "years_of_experience": 11,
        }
        form = CookCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_create_form_negative_experience_invalid(self):
        form_data = {
            "username": "new_user",
            "password1": "password123",
            "password2": "password123",
            "first_name": "First",
            "last_name": "Last",
            "email": "test@test.com",
            "years_of_experience": -3,
        }
        form = CookCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)

    def test_cook_update_form_valid(self):
        form_data = {
            "username": "updateduser",
            "first_name": "Updated",
            "last_name": "User",
            "years_of_experience": 4,
        }
        form = CookUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_update_form_negative_experience_invalid(self):
        form_data = {
            "username": "updateduser",
            "first_name": "Updated",
            "last_name": "User",
            "years_of_experience": -2,
        }
        form = CookUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)

    def test_dish_update_form_fields(self):
        form = DishUpdateForm()
        self.assertIn("cooks", form.fields)
        self.assertIn("ingredients", form.fields)
        self.assertTrue(
            isinstance(
                form.fields["cooks"],
                forms.ModelMultipleChoiceField
            )
        )
        self.assertTrue(
            isinstance(
                form.fields["ingredients"],
                forms.ModelMultipleChoiceField
            )
        )

    def test_cook_search_form_valid(self):
        form_data = {"username": "searchuser"}
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_search_form_valid(self):
        form_data = {"name": "Pizza"}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_type_search_form_valid(self):
        form_data = {"name": "Main Course"}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
