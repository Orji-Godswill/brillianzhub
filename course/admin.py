from django.contrib import admin
from .models import Course, Category, Module, Objective
# Register your models here.


admin.site.register(Course)

admin.site.register(Category)

admin.site.register(Module)

admin.site.register(Objective)
