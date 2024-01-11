from django.contrib import admin
from .models import CustomUser, FormData

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(FormData)