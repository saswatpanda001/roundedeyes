from django.contrib import admin
from movies.models import Movies,Category

admin.site.register(Movies)
admin.site.register(Category)