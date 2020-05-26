from django.contrib import admin
from .models import Todo


# Register your models here.
class Todo_admin(admin.ModelAdmin):
    list_display= ('id','text', 'complete' )

admin.site.register(Todo, Todo_admin)
