from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from restaurantKitchenService.models import DishType, Cook, Dish


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("year_of_expirience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("year_of_expirience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "license_number",
                    )
                },
            ),
        )
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name", "description", "price")
    list_filter = ("name", "description")
