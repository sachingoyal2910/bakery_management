from django.db import models
from users.models import Customer
from datetime import datetime
from django.utils import timezone

class Ingredient(models.Model):
    origin = [('Plant based', 'Plant based'), ('Animal Based', 'Animal Based')]
    measurement = [("gram", "gram"), ("litre", "litre"), ("kilogram", "kilogram"), ("Units", "Units")]
    name = models.CharField(help_text='Used to create bakery items', max_length=255, unique=True)
    type = models.CharField(max_length=70, choices=origin, default='Customer')
    unit = models.CharField(choices=measurement, help_text="unit of measurement of this ingredient", max_length=255, default="gram")
    price = models.FloatField(verbose_name="Cost Price of each unit")

    def __str__(self):
        return self.name + "(" + str(self.unit) + ")"

class IngredientPercentage(models.Model):
    ingredient = models.ForeignKey(Ingredient, blank=False, null=True, on_delete=models.SET_NULL)
    quantity = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.ingredient.name + " - " + str(self.quantity) + ' ' + str(self.ingredient.unit)

class BakeryItem(models.Model):
    name = models.CharField(help_text='name of item', max_length=255, unique=True)
    ingredients = models.ManyToManyField(IngredientPercentage, blank=True)
    cost_price = models.FloatField(null=True, blank=True)
    selling_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    item = models.ForeignKey(BakeryItem, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.id

class Order(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    order_items = models.ManyToManyField(OrderItem)
    bill = models.TextField(help_text='bill')
    amount_paid = models.FloatField(null=True, blank=True)
    amount_due = models.FloatField(null=True, blank=True)
    generated_date = models.DateTimeField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.id