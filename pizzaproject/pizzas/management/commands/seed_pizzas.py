from django.core.management.base import BaseCommand
from pizzas.models import Pizza

class Command(BaseCommand):
    def handle(self, *args, **options):
        pizzas = [
            { "name": "queen", "ingredients": ["🐷","🍄","🍅","🧀"] },
            { "name": "cheese", "ingredients": ["🧀","🍅"] },
            { "name": "oriental", "ingredients": ["🍅","🐑","🍄","🌶"] },
            { "name": "royal", "ingredients": ["🍅","🌵"] },
        ]

        for p in pizzas:
            Pizza.objects.get_or_create(
                name=p["name"],
                defaults={"ingredients": p["ingredients"]}
            )

        self.stdout.write(self.style.SUCCESS("Pizzas ajoutées !"))
