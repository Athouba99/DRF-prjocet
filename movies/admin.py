from django.contrib import admin
from movies.models import Movie, Booking
# Register your models here.

to_register = [ Movie, Booking,]

admin.site.register(to_register)