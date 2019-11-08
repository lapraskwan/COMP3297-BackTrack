from django.contrib import admin
from .models import sprint_backlog_item, capacity

# Register your models here.
admin.site.register(sprint_backlog_item)
admin.site.register(capacity)