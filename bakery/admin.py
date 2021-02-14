from django.contrib import admin
from bakery.models import Ingredient, IngredientPercentage, BakeryItem, Order, OrderItem

class BakeryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'all_ingredients', 'cost_price', 'selling_price')

    @staticmethod
    def all_ingredients(obj):
        all_ingredients = []
        for ingredient in obj.ingredients.all():
            all_ingredients.append(ingredient.__str__())
        return ' , '.join(all_ingredients)

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(IngredientPercentage)
admin.site.register(BakeryItem, BakeryItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
