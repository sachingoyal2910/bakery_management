from django.contrib import admin
from users.models import Customer
from users.models import User

# Register your models here.
admin.site.register(Customer)
admin.site.register(User)
