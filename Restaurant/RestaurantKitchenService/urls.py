from django.urls import path

from RestaurantKitchenService.views import AllDishView, AllCoockerView, AllDishTypesView, DishView, \
    DishTypeView, index, CreateDishView, UpdateDishView, DeleteDishView

urlpatterns = [
    path("", index, name="index"),
    path("dishes", AllDishView.as_view(), name="dishes"),
    path("dishes/create", CreateDishView.as_view(), name="create_dish"),
    path("dishes/<int:pk>/update", UpdateDishView.as_view(), name="update_dish"),
    path("dishes/<int:pk>/delete", DeleteDishView.as_view(), name="delete_dish"),
    path("coockers", AllCoockerView.as_view(), name="coockers"),
    path("dishesTypes", AllDishTypesView.as_view(), name="dishTypes"),
    path("dishes/<int:pk>/", DishView.as_view(), name="dish_view"),
    path("dishesTypes<int:pk>/", DishTypeView.as_view(), name="dishTypes_detail"),
]