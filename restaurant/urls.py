from django.urls import path, include

from .views import (
    IndexView,
    CookListView,
    DishListView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
]

app_name = "restaurant"
