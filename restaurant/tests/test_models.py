from django.test import TestCase

from restaurant.models import DishType, Cook, Ingredient, Dish


class ModelTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Pizza")
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = Cook.objects.create_user(
            username="test_username",
            password="Test1234",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(cook),
            f"{cook.username}: ({cook.first_name} {cook.last_name})"
        )

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(
            name="carrot",
            is_vegan=True,
            calories=25,
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Pizza",
        )
        dish = Dish.objects.create(
            name="Chicken Teriyaki",
            description="Grilled chicken glazed in teriyaki sauce",
            price=14.5,
            dish_type=dish_type,
        )
        self.assertEqual(
            str(dish),
            f"{dish.name} (price: {dish.price}, dish_type: {dish.dish_type})"
        )

    def test_create_cook_with_years_of_experience(self):
        username = "test_username"
        password = "Test1234"
        years_of_experience = 11
        cook = Cook.objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))
