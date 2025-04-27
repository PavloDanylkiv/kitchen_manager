from django.urls import path, include

from .views import (
    IndexView,
    CookListView,
    DishListView,
    DishTypeListView,
    DishDetailView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
]

app_name = "restaurant"
