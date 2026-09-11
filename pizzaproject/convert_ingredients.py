from pizzas.models import Pizza, Ingredient

for pizza in Pizza.objects.all():
    for ing_name in pizza.ingredients:  # ancien JSON
        ing, created = Ingredient.objects.get_or_create(
            name=ing_name,
            defaults={"price": 0, "calories": 0}
        )
        pizza.ingredients.add(ing)
