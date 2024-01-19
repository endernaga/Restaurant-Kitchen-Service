from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurantKitchenService.forms import (
    DishCreationForm,
    CookersCreationForm,
    DishTypeCreationForm,
    DishSearchForm,
    CookSearchForm,
    DishTypeSearchForm)
from restaurantKitchenService.models import DishType, Cook, Dish


class IndexView(generic.View):
    templates = "restaurantKitchenService/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        num_dishes = Dish.objects.count()

        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1

        context = {
            "num_dishes": num_dishes,
            "num_visits": self.request.session["num_visits"],
        }

        return context


@login_required
def index(request):
    num_dishes = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dishes": num_dishes,
        "num_visits": request.session["num_visits"],
    }

    return render(
        request,
        "restaurantKitchenService/index.html",
        context=context)


class AllDishView(generic.ListView):
    model = Dish
    context_object_name = "dishes"
    paginate_by = 5
    template_name = "restaurantKitchenService/dish_list.html"

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
    template_name = "restaurantKitchenService/dish_detail.html"


class CreateDishView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishCreationForm
    success_url = reverse_lazy("restaurant:dishes")


class UpdateDishView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishCreationForm
    success_url = reverse_lazy("restaurant:dishes")


class DeleteDishView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dishes")


class AllCookerView(generic.ListView):
    model = Cook
    context_object_name = "cookers"
    paginate_by = 5
    template_name = "restaurantKitchenService/cookers_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = CookSearchForm()
        return context

    def get_queryset(self):
        username = self.request.GET.get("username")
        if username:
            return Cook.objects.filter(username__icontains=username)
        return Cook.objects.all()


class CreateCookerView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookersCreationForm


class DetailCookerView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dish_set")


class AllDishTypesView(generic.ListView):
    model = DishType
    context_object_name = "dishTypes"
    paginate_by = 5
    template_name = "restaurantKitchenService/dishType_list.html"

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
    template_name = "restaurantKitchenService/dishType_detail.html"


class CreateDishTypeView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeCreationForm
    success_url = reverse_lazy("restaurant:dishTypes")


class UpdateDishTypeView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeCreationForm
    success_url = reverse_lazy("restaurant:dishTypes")


class DeleteDishTypeView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("restaurant:dishTypes")
