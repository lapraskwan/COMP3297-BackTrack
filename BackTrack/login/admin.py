from django.contrib import admin
from .models import user, currentUser

# Register your models here.
admin.site.register(user)
admin.site.register(currentUser)