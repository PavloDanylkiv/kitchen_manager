from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType, Cook, Dish

DISH_TYPE_URL = reverse("restaurant:dish-type-list")
COOK_URL = reverse("restaurant:cook-list")
DISH_URL = reverse("restaurant:dish-list")


class PublicDishTypeTests(TestCase):
    def test_login_requires(self):
        response = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(response.status_code, 200)


class PublicCookTests(TestCase):
    def test_login_requires(self):
        response = self.client.get(COOK_URL)
        self.assertNotEqual(response.status_code, 200)


class PublicDishTests(TestCase):
    def test_login_requires(self):
        response = self.client.get(DISH_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Pizza")
        DishType.objects.create(name="Pasta")
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "restaurant/dishtype_list.html")


class PrivateCookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_cooks(self):
        Cook.objects.create_user(
            username="test1",
            password="test123",
        )
        Cook.objects.create_user(
            username="test2",
            password="test234",
        )
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)
        cooks = Cook.objects.all()
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )
        self.assertTemplateUsed(response, "restaurant/cook_list.html")


class PrivateDishTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_dishes(self):
        cook1 = Cook.objects.create_user(
            username="test1",
            password="test123",
        )

        cook2 = Cook.objects.create_user(
            username="test2",
            password="test234",
        )

        dish_type1 = DishType.objects.create(name="Pasta")
        dish_type2 = DishType.objects.create(name="Pizza")
        dish1 = Dish.objects.create(
            name="Chicken Teriyaki",
            description="Grilled chicken glazed in teriyaki sauce",
            price=14.9,
            dish_type=dish_type1,
        )
        dish1.cooks.add(cook1)

        dish2 = Dish.objects.create(
            name="Margherita Pizza",
            description="Classic pizza with mozzarella and basil",
            price=19.9,
            dish_type=dish_type2,
        )
        dish2.cooks.add(cook2)

        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "restaurant/dish_list.html")
