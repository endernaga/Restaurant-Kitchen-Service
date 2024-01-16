from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from RestaurantKitchenService.forms import DishCreationForm, CookersCreationForm, DishTypeCreationForm, DishSearchForm, \
    CookSearchForm, DishTypeSearchForm
from RestaurantKitchenService.models import DishType, Cook, Dish


@login_required
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = DishSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return Dish.objects.filter(name__icontains=name)
        return Dish.objects.all()


class DishView(generic.DetailView):
    model = Dish
    context_object_name = "dish"
    template_name = "RestaurantKitchenService/dish_detail.html"

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


class AllCookerView(generic.ListView):
    model = Cook
    context_object_name = "cookers"
    paginate_by = 5
    template_name = "RestaurantKitchenService/cookers_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = CookSearchForm()
        return context

    def get_queryset(self):
        username = self.request.GET.get("username")
        if username:
            return Cook.objects.filter(username__icontains=username)
        return Cook.objects.all()


class CreateCookerView(generic.CreateView):
    model = Cook
    form_class = CookersCreationForm


class DetailCookerView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dish_set")


class AllDishTypesView(generic.ListView):
    model = DishType
    context_object_name = "dishTypes"
    paginate_by = 5
    template_name = "RestaurantKitchenService/dishType_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = DishTypeSearchForm()
        return context

    def get_queryset(self):
        name = self.request.GET.get("name")
        if name:
            return DishType.objects.filter(name__icontains=name)
        return DishType.objects.all()


class DishTypeView(generic.DetailView):
    model = DishType
    context_object_name = "dish"
    template_name = "RestaurantKitchenService/dishType_detail.html"


class CreateDishTypeView(generic.CreateView):
    model = DishType
    form_class = DishTypeCreationForm
    success_url = reverse_lazy("restaurant:dishTypes")


class UpdateDishTypeView(generic.UpdateView):
    model = DishType
    form_class = DishTypeCreationForm
    success_url = reverse_lazy("restaurant:dishTypes")


class DeleteDishTypeView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("restaurant:dishTypes")