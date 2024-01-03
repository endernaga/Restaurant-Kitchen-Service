from django.urls import path

from RestaurantKitchenService.views import AllDishView, AllCoocerView, AllDishTypesView

urlpatterns = [
    path("dishes", AllDishView.as_view(), name="dishes"),
    path("coockers", AllCoocerView.as_view(), name="coockers"),
    path("dishesTypes", AllDishTypesView.as_view(), name="dishes"),
]