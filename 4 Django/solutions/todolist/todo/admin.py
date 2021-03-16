from django.contrib import admin

# Register your models here.
from .models import Priority, TodoItem


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('priority', 'text', 'created_date', 'completed_date')


class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


admin.site.register(Priority, PriorityAdmin)
admin.site.register(TodoItem, TodoItemAdmin)
