from django.urls import path
from .views import (
    PizzaListApi,
    PizzaDetailByNameApi,
    PizzaByIngredientApi,
    PizzaByIngredientsApi
)

print(">>> pizzas.urls LOADED")  # doit être AVANT urlpatterns

urlpatterns = [
    path('pizzas/', PizzaListApi.as_view()),
    path('pizzas/filter/', PizzaByIngredientsApi.as_view()),
    path('pizzas/ingredient/<str:ingredient>/', PizzaByIngredientApi.as_view()),
    path('pizzas/<str:name>/', PizzaDetailByNameApi.as_view()),
]

