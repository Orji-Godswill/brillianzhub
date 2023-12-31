from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # Number of choices displayed for each question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['course', 'module', 'order']
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
