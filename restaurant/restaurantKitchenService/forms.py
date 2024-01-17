from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from restaurantKitchenService.models import DishType, Cook, Dish


class DishTypeCreationForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = "__all__"


class CookersCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "year_of_expirience",
        )


class DishCreationForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(required=False, max_length=255)


class CookSearchForm(forms.Form):
    username = forms.CharField(required=False, max_length=255)


class DishSearchForm(forms.Form):
    name = forms.CharField(required=False, max_length=255)
