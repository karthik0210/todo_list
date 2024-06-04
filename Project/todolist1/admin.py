# from django.contrib import admin
# from .models import Task

# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'status', 'due_date')
#     list_filter = ('status', 'due_date')
#     search_fields = ('name', 'description')


from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status', 'created_at')  # Remove 'due_date' if not needed
    list_filter = ('status',)  # Remove 'due_date' if not needed

admin.site.register(Task, TaskAdmin)


