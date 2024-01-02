from django.urls import path

from RestaurantKitchenService.views import AllDishView

urlpatterns = [
    path("dishes", AllDishView.as_view(), name="dishes")
]