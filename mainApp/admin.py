from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    fields = ["category", "user", "title", "description", "complete"]
    list_display = ["category", "user"]

admin.site.register(Task, TaskAdmin)

# Register your models here.
