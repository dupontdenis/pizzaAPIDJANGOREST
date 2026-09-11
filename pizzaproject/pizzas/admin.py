
from django.contrib import admin
from .models import Pizza, Ingredient

class IngredientInline(admin.TabularInline):
    model = Pizza.ingredients.through
    extra = 1
    verbose_name = "Ingrédient"
    verbose_name_plural = "Ingrédients"

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ("name", "get_ingredients", "get_total_price", "get_total_calories")
    search_fields = ("name", "ingredients__name")
    list_filter = ("ingredients__name",)
    inlines = [IngredientInline]

    def get_ingredients(self, obj):
        return ", ".join(i.name for i in obj.ingredients.all())
    get_ingredients.short_description = "Ingrédients"

    def get_total_price(self, obj):
        return f"{sum(i.price for i in obj.ingredients.all()):.2f} €"
    get_total_price.short_description = "Prix total"

    def get_total_calories(self, obj):
        return sum(i.calories for i in obj.ingredients.all())
    get_total_calories.short_description = "Calories totales"



@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "calories")
    search_fields = ("name",)
    list_filter = ("price", "calories")