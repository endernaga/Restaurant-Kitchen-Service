from django.urls import path

from restaurantKitchenService.views import (
    AllDishView,
    AllCookerView,
    AllDishTypesView,
    DishView,
    DishTypeView,
    index,
    CreateDishView,
    UpdateDishView,
    DeleteDishView,
    CreateDishTypeView,
    UpdateDishTypeView,
    DeleteDishTypeView,
    DetailCookerView,
    CreateCookerView)

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", AllDishView.as_view(), name="dishes"),
    path("dishes/create/", CreateDishView.as_view(), name="create_dish"),
    path(
        "dishes/<int:pk>/update/",
        UpdateDishView.as_view(),
        name="update_dish"),
    path(
        "dishes/<int:pk>/delete/",
        DeleteDishView.as_view(),
        name="delete_dish"),
    path("cookers/", AllCookerView.as_view(), name="cookers"),
    path(
        "cookers/<int:pk>/",
        DetailCookerView.as_view(),
        name="cookers_detail"),
    path("cookers/create/", CreateCookerView.as_view(), name="cookers_create"),
    path("dishesTypes/", AllDishTypesView.as_view(), name="dishTypes"),
    path(
        "dishesTypes/create/",
        CreateDishTypeView.as_view(),
        name="dishTypes_create"),
    path(
        "dishesTypes/<int:pk>/update/",
        UpdateDishTypeView.as_view(),
        name="dishTypes_update"),
    path(
        "dishesTypes/<int:pk>/delete/",
        DeleteDishTypeView.as_view(),
        name="dishTypes_delete"),
    path("dishes/<int:pk>/", DishView.as_view(), name="dish_view"),
    path("dishesTypes/<int:pk>/",
         DishTypeView.as_view(), name="dishTypes_detail"),
]
