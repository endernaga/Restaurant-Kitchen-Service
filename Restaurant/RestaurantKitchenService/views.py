from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from RestaurantKitchenService.forms import DishCreationForm
from RestaurantKitchenService.models import DishType, Cook, Dish


def index(request):
    num_dishes = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context ={
        "num_dishes": num_dishes,
        "num_visits": request.session["num_visits"],
    }

    return render(request, "RestaurantKitchenService/index.html", context=context)

class AllDishView(generic.ListView):
    model = Dish
    context_object_name = "dishes"
    paginate_by = 5
    template_name = "RestaurantKitchenService/dish_list.html"


class CreateDishView(generic.CreateView):
    model = Dish
    form_class = DishCreationForm
    success_url = reverse_lazy("restaurant:dishes")


class UpdateDishView(generic.UpdateView):
    model = Dish
    form_class = DishCreationForm
    success_url = reverse_lazy("restaurant:dishes")


class DeleteDishView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dishes")


class AllCoockerView(generic.ListView):
    model = Cook
    context_object_name = "coockers"
    paginate_by = 5
    template_name = "RestaurantKitchenService/coockers_list.html"


class AllDishTypesView(generic.ListView):
    model = DishType
    context_object_name = "dishTypes"
    paginate_by = 5
    template_name = "RestaurantKitchenService/dishType_list.html"


class DishView(generic.DetailView):
    model = Dish
    context_object_name = "dish"
    template_name = "RestaurantKitchenService/dish_detail.html"


class DishTypeView(generic.DetailView):
    model = DishType
    context_object_name = "dish"
    template_name = "RestaurantKitchenService/dishType_detail.html"