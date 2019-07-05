from django.contrib import admin

# Register your models here.
from .models import Forecast

admin.site.register(Forecast)