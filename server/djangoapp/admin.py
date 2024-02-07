from django.contrib import admin
from .models import CarMake, CarModel

class CarModelAdmin(admin.ModelAdmin):
    fields = ['dealer_id', 'name', 'type', 'date']

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]

admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)
