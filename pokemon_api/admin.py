from django.contrib import admin
from pokemon_api import models
# Register your models here.


admin.site.register(models.Pokemon)
admin.site.register(models.Evolution)