from django.shortcuts import render
from django.views import generic

from RestaurantKitchenService.models import DishType


class AllDishView(generic.ListView):
    model = DishType
    context_object_name = "dishes"
    paginate_by = 5
    template_name = "restaurant/dish_list.html"
