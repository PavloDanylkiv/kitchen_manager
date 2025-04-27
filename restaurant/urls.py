from django.urls import path, include

from .views import IndexView, CookListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cooks/", CookListView.as_view(), name="cook-list")
]

app_name = "restaurant"
