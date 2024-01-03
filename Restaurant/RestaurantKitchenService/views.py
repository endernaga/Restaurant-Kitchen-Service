from django.shortcuts import render
from django.views import generic

from RestaurantKitchenService.models import DishType, Cook, Dish


class AllDishView(generic.ListView):
    model = Dish
    context_object_name = "dishes"
    paginate_by = 5
    template_name = "restaurant/dish_list.html"


class AllCoocerView(generic.ListView):
    model = Cook
    context_object_name = "coockers"
    paginate_by = 5
    template_name = "restaurant/coockers_list.html"


class AllDishTypesView(generic.ListView):
    model = DishType
    context_object_name = "dishTypes"
    paginate_by = 5
    template_name = "restaurant/dishType_list.html"
